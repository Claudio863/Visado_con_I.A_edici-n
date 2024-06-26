import os# pip install google-cloud-documentai
import sys
from google.cloud import documentai
from google.api_core.client_options import ClientOptions
import os
from PyPDF2 import PdfReader, PdfWriter
import streamlit as st
import pandas as pd
import time
import shutil
from PIL import Image
sys.path.append( '../Pag_web' )
from Enviar_registro_F_T import envio_registro_F_T 
import Funciones_OCR as ocr
import Proceso_filtro as chat_gpt
from Enviar_registro_F_T import registrar_error
from docx import Document


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='Pag_web/google_ocr.json'



#path_document=r"C:\Users\cgomez\Desktop\Proyectos\Automatización_de_procesos\Scan\data_scan\matriz.pdf"
#ode_path=r"C:\Users\cgomez\Desktop\Proyectos\Automatización_de_procesos\Scan\ode.pdf"
path_origen="Pag_web/"
image_path =path_origen+ "Images/creditu_logo.jpg"
image = Image.open(image_path)
resized_image = image.resize((100, 100))  # Cambia el tamaño de la imagen a 300x300 píxeles
st.image(resized_image)

st.header("Datos Operacionales")
#rut_cliente=st.text_input("Ingrese el rut del cliente")
ejecutivo = st.selectbox(
    'Nombre del operador',
    ('Claudia_Castro', 'Christian_Guerra', 'Diglis_Rosal'))


st.header("Visado Escritura Scan con I.A")
borrador = st.file_uploader("Seleccionar Borrador en formato PDF", type=["txt", "pdf", "docx"])
ode = st.file_uploader("Seleccionar ODE en formato PDF", type=["txt", "pdf"])

# ...
#docx_path = None  # Define docx_path with a default value

if borrador is not None:
    docx_path="Pag_web/data_borrador/borrador.docx"
    with open(os.path.join("Pag_web/data_borrador/", "borrador.docx"), "wb") as f:
        f.write(borrador.getvalue())

if ode is not None:
    ode_path="Pag_web/data_borrador/ode.pdf"
    with open(os.path.join("Pag_web/data_borrador", "ode.pdf"), "wb") as f:
        f.write(ode.getvalue())
        
## Logo de botón
image_path_b = path_origen+"Images/Logo_oficial.png"
image_b = Image.open(image_path_b)
col1, col2 = st.columns([21, 9])
col1.image(image_b, use_column_width=True)
try:
    if st.button("Comparar con I.A :robot_face:"):
        start_time = time.time()
        #st.write(files_and_directories)
        text=""
        def leer_docx(docx_path):
            # Cargar el documento DOCX
            doc = Document(docx_path)

            # Inicializar una cadena para almacenar el contenido del documento
            text = ""

            # Iterar a través de los párrafos del documento y agregarlos a la cadena
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"

            return text

        if __name__ == "__main__":
            # Ruta del archivo DOCX
            # Leer el contenido del archivo DOCX y almacenarlo en la variable text
            text = leer_docx(docx_path)

        print(text)
        entrenamiento_path="Pag_web/Entrenamiento_previo_prueba.tsv"
        Entrenam=pd.read_csv(entrenamiento_path,sep='\t',encoding='utf-8')
        # Assuming you have a dataframe called 'df'
        
        progress_text = "Comparando el documento..."
        df, respuesta_general_borrador, cost, prompts, ode_tabulada = chat_gpt.proceso(text=text,Entrenam=Entrenam,ode_path=ode_path)
        print(df)
        
        def color_comparacion(val):
                    if val == 'IGUAL':
                        return 'background-color: green; color: white'
                    elif val == 'NO IGUAL':
                        return 'background-color: red; color: white'
                    else:
                        return ''
        # Display the dataframe in Streamlit
        #my_bar.empty()
        st.dataframe(df.style.applymap(color_comparacion))
        # Delete all files in the directory
        folder_path = "Pag_web/Paginas"
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        elapsed_time = time.time() - start_time

        id_operacion=envio_registro_F_T(df,ejecutivo,respuesta_general_borrador,ode_tabulada,str(elapsed_time))
        st.code(id_operacion, language="python")
except Exception as e:
    elapsed_time = time.time() - start_time
    import traceback
    st.error("Ops! Algo salió mal, por favor revisa que los documentos sean los adecuados e intenta nuevamente. Tu error ha sido reportado.")
    st.image("Pag_web/Images/Error.jpeg", width=300)
    registrar_error(ejecutivo+"_visado_escritura", str(elapsed_time)+"_" +str(e)+traceback.format_exc())
    st.write(str(e))

