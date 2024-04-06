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
def split_pdf_pages(file_path, paginas_path):
    pages = []
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            output_file_path = os.path.join(paginas_path, f"page_{page_num + 1}.pdf")
            with open(output_file_path, 'wb') as output_file:
                writer.write(output_file)
            pages.append(output_file_path)
    return pages

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='Pag_web/spherical-park-415115-1b5c59410476.json'



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
borrador = st.file_uploader("Seleccionar Escritura en formato PDF", type=["txt", "pdf", "docx"])
ode = st.file_uploader("Seleccionar ODE en formato PDF", type=["txt", "pdf"])

# ...

if borrador is not None:
    docx_path="Pag_web/data_scan/scan.pdf"
    with open(os.path.join("Pag_web/data_scan/", "scan.pdf"), "wb") as f:
        f.write(borrador.getvalue())

if ode is not None:
    ode_path="Pag_web/data_scan/ode.pdf"
    with open(os.path.join("Pag_web/data_scan", "ode.pdf"), "wb") as f:
        f.write(ode.getvalue())
        
## Logo de botón
image_path_b = path_origen+"Images/Logo_oficial.png"
image_b = Image.open(image_path_b)
col1, col2 = st.columns([21, 9])
col1.image(image_b, use_column_width=True)
if st.button("Comparar con I.A :robot_face:"):
    file_path = docx_path
    paginas_path = "Pag_web/Paginas"
    page_list = ocr.split_pdf_pages(file_path, paginas_path)
    files_and_directories = os.listdir(paginas_path)
    #st.write(files_and_directories)
    text=""
    progress_text = "OCR procesando documento escaneado... :mag_right: 	:memo:  "
    st.write(progress_text)
    

    my_bar = st.progress(0, text=progress_text)
    for page in page_list:
        p_avance= page_list.index(page)/len(page_list)
        p_avance=p_avance*100
        #p_avance=p_avance/3
        truncado = int(p_avance)
        my_bar.progress(truncado)
        

        #st.write(page)
        text_agregar=ocr.get_text_from_pdf_ocr(page)
        text=text+"\n"+text_agregar
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
    id_operacion=envio_registro_F_T(df,ejecutivo,respuesta_general_borrador,ode_tabulada)
    st.code(id_operacion, language="python")


