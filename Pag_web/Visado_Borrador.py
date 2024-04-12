import streamlit as st
from docx import Document
import PyPDF2
import re
from docx import Document
from PyPDF2 import PdfReader
import openai
import pandas as pd
import time
from io import StringIO
import time

import openai
import os
import streamlit as st
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from Google import Create_Service_With_Service_Account
import pandas as pd
import random
import time
import streamlit as st 
import os

from PIL import Image
path_origen="Pag_web/"
image_path =path_origen+ "Images/creditu_logo.jpg"
image = Image.open(image_path)
resized_image = image.resize((100, 100))  # Cambia el tamaño de la imagen a 300x300 píxeles
st.image(resized_image)

csv_file_path =path_origen+ "Entrenamiento_previo_prueba.tsv"
Entrenam = pd.read_csv(csv_file_path, sep='\t', encoding='utf-8')
st.header("Datos Operacionales")
#rut_cliente=st.text_input("Ingrese el rut del cliente")
ejecutivo = st.selectbox(
    'Nombre del operador',
    ('Claudia_Castro', 'Christian_Guerra', 'Diglis_Rosal'))


def main():
    import streamlit as st
    import os
    
    st.header("Visado Borrador escritura con I.A")
    borrador = st.file_uploader("Seleccionar Borrador en formato DOCX", type=["txt", "pdf", "docx"])
    ode = st.file_uploader("Seleccionar ODE en formato PDF", type=["txt", "pdf"])

    # ...

    if borrador is not None:
        docx_path=path_origen+"data_borrador/borrador.docx"
        with open(os.path.join(path_origen+"data_borrador", "borrador.docx"), "wb") as f:
            f.write(borrador.getvalue())

    if ode is not None:
        ode_path=path_origen+"data_borrador/ode.pdf"
        with open(os.path.join(path_origen+"data_borrador", "ode.pdf"), "wb") as f:
            f.write(ode.getvalue())

        #Imágen botón
    image_path_b = path_origen+"Images/Logo_oficial.png"
    image_b = Image.open(image_path_b)
    col1, col2 = st.columns([21, 9])
    col1.image(image_b, use_column_width=True)
    if st.button("Comparar con I.A :robot_face:"):
        progress_text = "Comparando el documento..."
        my_bar = st.progress(0, text=progress_text)
        my_bar.progress(0, text=progress_text+":robot_face:"+ "0%")
        import openai
        api_keyx=st.secrets["API_KEY_OPENAI"]

        if borrador is not None and ode is not None:
            # Aquí puedes agregar el código que deseas ejecutar con los documentos cargados
            # Utiliza doc1 y doc2 para acceder a los contenidos de los documentos
            #progress_text = "Comparando documentos...   "
            #my_bar = st.progress(0, text=progress_text)


            import time

            start_time = time.time()  # Guarda el tiempo actual
            res_muestra1_ode="""
            Inmobiliaria(s) Vendedora(s):
            - Nombre: Isiete Metropolitana II Spa
            - Rut: 77.029.265-4
            - Banco Alzante: Banco Consorcio

            Nombre del Proyecto:
            - Condominio Parque Sole Sector II

            Deudor:
            - Nombre: Aurelia Constanza Madrid Silva
            - Cédula Nacional: 18.200.820-6
            - Nacionalidad: Chilena
            - Profesión: Profesora
            - Estado Civil: Soltero(a)

            Seguros:
            -Seguro Desgravamen: Si, 0,15 UF
            -Seguro Incendio/Sismo: Si, 0,48 UF
            -Seguro Cesantia: Si, 0,96 UF
            -Seguro Credito: Si, 0,00 UF

            Datos del Crédito (en UF):
            - Precio venta: 2.625 UF
            - Monto líquido: 1.959,83 UF
            - Monto bruto: 1.959,83 UF
            - Gastos operacionales del préstamo: 0 UF
            - Cuota contado: 260,17 UF
            - Precio venta estacionamiento: 425 UF
            - Precio tasación estacionamiento: 380 UF
            - Precio venta bodega: -
            - Precio tasación bodega: -
            - Plazo del crédito: 30 años
            - Meses de gracia: 5
            - Cuota dividendo sin seguro (inicial): 12,54 UF
            - Cuota dividendo sin seguro (final): 13,13 UF
            - Tasa de interés: 6,51 %

            Desglose Subsidio:
            - Tipo de subsidio: DS19
            - Subsidio base: 125,00
            - Subsidio integración: 100,00
            - Subsidio captación: 100,00
            - Monto total subsidio: 325,00
            - Ahorro previo: 80,00


            Mandatario:
            - Nombre: Rene Orlando Cabezas Parra
            - Rut: 15.777.029-2
            - Estado Civil: Soltero(a)
            - Profesión: Ingeniero En Prevención De Riesgos
            - Dirección: CALLE OLLANTAY, PORTAL DEL INCA V 2752, Calama, El Loa, Región de Antofagasta

            Codeudor:
            - Nombre: Rene Orlando Cabezas Parra
            - Rut: 15.777.029-2
            - Estado Civil: Soltero(a)
            - Profesión: Ingeniero En Prevención De Riesgos
            - Dirección: CALLE OLLANTAY, PORTAL DEL INCA V 2752, Calama, El Loa, Región de Antofagasta

            Datos del inmueble:
            - Número: 103
            - Torre: K
            - Dirección: Av. Los Sauces 2520, Padre Hurtado, Talagante
            - Rol: 00139-00127
            - Lote: -
            - Manzana: -

            Gastos operacionales:

            Estimados:
                -Tasación: 0,00 UF
                -Estudio de Titulos: 0,00 UF
                -Escrituracion: 3,55 UF
                -Notaria: 3,00 UF
                -Impuesto: 0,00 UF

            Provisionado:
                - Tasación: 0,00 UF
                -Estudio de Titulos: 0,00 UF
                -Escrituracion: 3,55 UF
                -Notaria: 0,00 UF
                -Impuesto: 0,00 UF

            """
            res_muestra2_ode="""
            Inmobiliaria(s) Vendedora(s):
            - Nombre: Inmobiliaria Sur Cincuenta Y Dos Spa
            - Rut: 77.029.495-9
            - Banco Alzante: Banco Chile

            Nombre del Proyecto:
            - Bosques De San Bernardo

            Deudor:
            - Nombre: Yerardi Patricia Friz Arancibia
            - Cédula Nacional: 16.971.902-0
            - Nacionalidad: Chilena
            - Profesión: Carabinero Auxiliar De Enfermería
            - Estado Civil: Soltero(a)

            Seguros:
            - Seguro Desgravamen: Sí, valor 0,06 UF
            - Seguro Incendio/Sismo: Sí, valor 0,26 UF
            - Seguro Cesantia: Sí, valor 0,39 UF
            - Seguro Credito: Sí, valor 0,00 UF

            Mandatario:
            - Nombre: Helén Liliana Friz Arancibia
            - Rut: 13.988.311-K
            - Dirección: PASAJE COYA 14095, San Bernardo, Maipo, Región Metropolitana de Santiago
            - Estado Civil: Casado, Sociedad Conyugal
            - Profesión: Empleado
            - Nacionalidad: Chilena

            Datos del Crédito (en UF):
            - Precio venta: 1.400 UF
            - Monto líquido: 789,95 UF
            - Monto bruto: 789,95 UF
            - Gastos operacionales del préstamo: 0 UF
            - Cuota contado: 0 UF
            - Precio venta estacionamiento: -
            - Precio tasación estacionamiento: -
            - Precio venta bodega: -
            - Precio tasación bodega: -
            - Plazo del crédito: 30 años
            - Meses de gracia: 5
            - Cuota dividendo sin seguro (inicial): 5,76 UF
            - Cuota dividendo sin seguro (final): 6,08 UF
            - Tasa de interés: 7,83 %

            Desglose Subsidio:
            - Tipo de subsidio: DS19
            - Subsidio base: 200,00
            - Subsidio integración: 100,00
            - Subsidio captación: 150,00
            - Monto total subsidio: 450,00
            - Ahorro previo: 160,05

            Datos del inmueble:

            -Número: 207
            -Torre: 3
            -Dirección: CAMINO LA VARA 02600
            -Rol: 4570-179
            -Lote: -
            -Manzana: Piso 2

            Gastos operacionales:

            Estimados:
                - Tasación: 3,00 UF
                - Estudio de Titulos: 2,50 UF
                - Escrituración: 3,20 UF
                - Notaria: 3,00 UF
                - Impuesto: 0,00 UF

            Provisionado:
                - Tasación: 3,00 UF
                - Estudio de Titulos: 2,50 UF
                - Escrituración: 3,20 UF
                - Notaria: 0,00 UF
                - Impuesto: 0,00 UF
                """
            res_muestra3_ode="""
            Inmobiliaria(s) Vendedora(s):
            - Nombre: Inmobiliaria Isiete Maule I Spa
            - Rut: 77.009.211-6
            - Banco Alzante: Banco Chile

            Nombre del Proyecto:
            - Mirador Urbano

            Deudor:
            - Nombre: Eliseo Rene Salazar Valdés
            - Cédula Nacional: 18.743.613-3
            - Nacionalidad: Chilena
            - Profesión: Ingeniero En Informática Empresarial
            - Estado Civil: Soltero(a)

            Seguros:
            - Seguro Desgravamen: Sí, 0,16 UF
            - Seguro Incendio/Sismo: Sí, 0,53 UF
            - Seguro Cesantia: Sí, 0,98 UF
            - Seguro Crédito: Sí, 0,00 UF

            Datos del Crédito (en UF):
            - Precio venta: 2.500 UF
            - Monto líquido: 2.000 UF
            - Monto bruto: 2.000 UF
            - Gastos operacionales del préstamo: 0 UF
            - Cuota contado: 95 UF
            - Precio venta estacionamiento: 300 UF
            - Precio tasación estacionamiento: 360 UF
            - Precio venta bodega: -
            - Precio tasación bodega: -
            - Plazo del crédito: 30 años
            - Meses de gracia: 5
            - Cuota dividendo sin seguro (inicial): 13,48 UF
            - Cuota dividendo sin seguro (final): 14,26 UF
            - Tasa de interés: 7,02 %

            Desglose Subsidio:
            - Tipo de subsidio: DS19
            - Subsidio base: 125,00
            - Subsidio integración: 100,00
            - Subsidio captación: 100,00
            - Monto total subsidio: 325,00
            - Ahorro previo: 80,00

            Mandatario:
            - Nombre: Jimena Del Carmen Vasquez Caro
            - Rut: 16.001.763-5
            - Estado Civil: Soltero(a)
            - Profesión: Profesora De Matemáticas
            - Dirección: VOLCÁN LONQUIMAY 1677, Villa Los Volcanes, San Javier, Linares, Región del Maule

            Codeudor:
            - Nombre: Jimena Del Carmen Vasquez Caro
            - Rut: 16.001.763-5
            - Estado Civil: Soltero(a)
            - Profesión: Profesora De Matemáticas
            - Dirección: VOLCÁN LONQUIMAY 1677, Villa Los Volcanes, San Javier, Linares, Región del Maule

            Datos del inmueble:
            - Número: 406
            - Torre: B
            - Dirección: Calle 4 Oriente 831
            - Rol: 586-154
            - Lote: -
            - Manzana: Piso 4

            Gastos operacionales:
            Estimados:
                -Tasación: 3,00 UF
                -Estudio de Títulos: 2,50 UF
                -Escrituración: 3,20 UF
                -Notaria: 3,00 UF
                -Impuesto: 4,00 UF

            Provisionado:
                - Tasación: 3,00 UF
                -Estudio de Títulos: 2,50 UF
                -Escrituración: 3,20 UF
                -Notaria: 0,00 UF
                -Impuesto: 0,00 UF
            """
            res_muestra4_ode="""
            Inmobiliaria(s) Vendedora(s):
            - Nombre: Constructora Pocuro Spa
            - Rut: 79.840.820-8
            - Banco Alzante: -

            Nombre del Proyecto:
            - Portal Del Sur Etapa V

            Deudor:
            - Nombre: Francisco Javier Valentin Araya Miranda
            - Cédula Nacional: 16.683.666-2
            - Nacionalidad: Chilena
            - Profesión: Constructor Civil
            - Estado Civil: Casado, Separación Total De Bienes

            Seguros:
            - Seguro Desgravamen: Sí, 0,13 UF
            - Seguro Incendio/Sismo: Sí, 0,38 UF
            - Seguro Cesantia: Sí, 0,81 UF
            - Seguro Credito: Sí, 0,00 UF

            Datos del Crédito (en UF):
            - Precio venta: 2.200 UF
            - Monto líquido: 1.644,94 UF
            - Monto bruto: 1.644,94 UF
            - Gastos operacionales del préstamo: 0 UF
            - Cuota contado: 50,06 UF
            - Precio venta estacionamiento: -
            - Precio tasación estacionamiento: -
            - Precio venta bodega: -
            - Precio tasación bodega: -

            Desglose Subsidio:
            - Tipo de subsidio: DS19
            - Subsidio base: 125,00
            - Subsidio integración: 200,00
            - Subsidio captación: 100,00
            - Monto total subsidio: 425,00
            - Ahorro previo: 80,00

            Mandatario:
            - Nombre: Matias Ignacio Araya Miranda
            - Rut: 19.285.906-9
            - Estado Civil: Soltero(a)
            - Profesión: Empleado
            - Dirección: Via El Mediterraneo 2097, Puerto Montt, Llanquihue, Región de Los Lagos

            Codeudor:
            -Nombre: -
            -Rut: -
            -Estado Civil: -
            -Profesión: -
            -Dirección: -

            Datos del inmueble:
            - Número: 480
            - Torre: B
            - Dirección: Constantino Kochifas Carcamo 480
            - Rol: 07568-00012
            - Lote: 12
            - Manzana: H5

            Gastos operacionales:

            Estimados:
                -Tasación: 0,00 UF
                -Estudio de Titulos: 0,00 UF
                -Escrituración: 3,55 UF
                -Notaria: 3,00 UF
                -Impuesto: 0,00 UF

            Provisionado:
                - Tasación: 0,00 UF
                -Estudio de Titulos: 0,00 UF
                -Escrituración: 3,55 UF
                -Notaria: 0,00 UF
                -Impuesto: 0,00 UF
            """
            def extrac_fragmento(palabra_incial, palabra_final, texto):
                palabras = texto.split()
                #print(palabras)
                palabra_inicio = palabra_incial
                palabra_final = palabra_final
                encabezado = 0
                indice_final = 0
                indice_inicial=0

                # Define la lista de palabras y el fragmento de búsqueda


                # Usa una comprensión de lista para encontrar los índices
                indice_inicial = [i for i, palabra in enumerate(palabras) if palabra.startswith(palabra_inicio)]
                indice_inicial=indice_inicial[0]
                indice_final = [i for i, palabra in enumerate(palabras) if palabra.startswith(palabra_final)]

                print("Índice inicial:", indice_inicial)
                print("Índice final:", indice_final)
                indice_final=indice_final[0]

                # Verifica que los índices no sean iguales
                if indice_inicial < indice_final:
                    fragmento_texto= ' '.join(palabras[indice_inicial:indice_final + 1])
                    print("Fragmento de texto entre las palabras buscadas:")
                #    print(fragmento_texto_encabezado)
                else:
                    print("Error: Los índices inicial y final no son válidos.")
                print(fragmento_texto)

                return fragmento_texto
            def string_to_dataframe(string, inde=None):
                data_dict = eval(string)

                # Convertir el diccionario en un DataFrame
                if inde is None:
                    df = pd.DataFrame(data_dict)
                else:
                    df = pd.DataFrame(data_dict, index=inde)

                return df
            def filtrar_fragmento_por_secuencia(texto, secuencia_inicio, secuencia_fin):
                # Construir el patrón regex
                patron = re.compile(f'{re.escape(secuencia_inicio)}(.*?){re.escape(secuencia_fin)}', re.DOTALL | re.IGNORECASE)

                # Buscar todas las coincidencias en el texto
                coincidencias = patron.findall(texto)

                # Devolver la lista de fragmentos encontrados
                return coincidencias
            def extract_substring(s, start, end):
                start_index = s.find(start)
                if start_index == -1:  # La secuencia de inicio no se encontró
                    return None
                start_index += len(start)  # Mover el índice de inicio al final de la secuencia de inicio

                end_index = s.find(end, start_index)
                if end_index == -1:  # La secuencia de final no se encontró
                    return None

                return s[start_index:end_index].strip()  # Extraer el fragmento y eliminar los espacios en blanco al principio y al final
            def separate_text(text):
                index = text.find("\n \nOBSERVACIONES")
                if index != -1:
                    text_ode_muestra1 = text[:index]
                    observaciones_ode = text[index + len("\n \nOBSERVACIONES"):]
                    return text_ode_muestra1, observaciones_ode
                else:
                    return text, ""

            def leer_pdf(pdf_path):
                            # Abrir el archivo PDF en modo lectura binaria
                            with open(pdf_path, 'rb') as pdf_file_obj:
                                # Crear un objeto PdfReader
                                pdf_reader = PdfReader(pdf_file_obj)

                                # Inicializar una cadena para almacenar el contenido del PDF
                                text = ""

                                # Iterar a través de las páginas del PDF y extraer el texto
                                for page in pdf_reader.pages:
                                    text += page.extract_text()
                            return text
            def mensaje(indice):
                Men=Entrenam[Entrenam["Operacion"]==indice]["Mensajes"]
                inde=Men.index[0]
            #print(inde)
                Men=eval(Men[inde])
                return Men

            ## Función que permite extraer fragmento independiente de si es una palabra o una secuencia de palabras
            def extract_text_fragment(text, start_sequence, end_sequence):
                start_index = text.find(start_sequence)
                if start_index == -1:  # Start sequence not found
                    return None
                start_index += len(start_sequence)  # Move start index to the end of the start sequence

                end_index = text.find(end_sequence, start_index)
                if end_index == -1:  # End sequence not found
                    return None

                return text[start_index:end_index].strip()  # Extract the fragment and remove leading/trailing whitespace


            #####################################################Realizar for para cada carpeta fine-tunning

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

            text_ode = leer_pdf(ode_path)
            text_ode,observaciones=separate_text(text_ode)
                # Imprimir el contenido
                # print(text)

            ### Tabulación ODE
            #(Marketing)
            api_keyx=st.secrets["API_KEY_OPENAI"]
            #(Operaciones)
            Mensajes_tab_ode=mensaje("Tab_ode")

            prompt = """Estructura este texto en el formato:
            Inmobiliaria(s) Vendedora(s):

            - Nombre:
            - Rut:
            - Banco Alzante: (Si no se encuentra el dato colocar un -)

            Nombre del Proyecto:

            - Condominio Parque Sole Sector II

            Deudor:

            - Nombre:
            - Cédula Nacional:
            - Nacionalidad:
            - Profesión:
            - Estado Civil:

            Seguros:
            -Seguro Desgravamen:
            -Seguro Incendio/Sismo:
            -Seguro Cesantia:
            -Seguro Credito:

            Datos del Crédito (en UF):

            - Precio venta:
            - Monto líquido:
            - Monto bruto:
            - Gastos operacionales del préstamo:
            - Cuota contado:
            - Precio venta estacionamiento: (Si no se encuentra el dato colocar un -)
            - Precio tasación estacionamiento: (Si no se encuentra el dato colocar un -)
            - Precio venta bodega: (Si no se encuentra el dato colocar un -)
            - Precio tasación bodega: (Si no se encuentra el dato colocar un -)
            -Plazo del crédito:
            -Meses de gracia:
            -Cuota dividendo sin seguro (inicial):
            -Cuota dividendo sin seguro (final):
            -Tasa de interés:

            Desglose Subsidio:
            -Tipo de subsidio:
            -Subsidio base:
            -Subsidio integración:
            -Subsidio captación:
            -Monto total subsidio:
            -Ahorro previo:


            Mandatario:

            -Nombre:
            -Rut:
            -Estado Civil:
            -Profesión:
            -Dirrección:

            Codeudor:

            -Nombre: (Si no se encuentra el dato colocar un -)
            -Rut: (Si no se encuentra el dato colocar un -)
            -Estado Civil: (Si no se encuentra el dato colocar un -)
            -Profesión: (Si no se encuentra el dato colocar un -)
            -Dirección: (Si no se encuentra el dato colocar un -)

            Datos del inmueble:

            -Número:
            -Torre: (Si no se encuentra el dato colocar un -)
            -Dirección:
            -Rol:
            -Lote: (Si no se encuentra el dato colocar un -)
            -Manzana: (Si no se encuentra el dato colocar un -)

            Gastos operacionales:

            Estimados:
                - Tasación:
                - Estudio de Títulos:
                - Escrituración:
                - Notaria:
                - Impuesto:

            Provisionado:
                - Tasación:
                - Estudio de Títulos:
                - Escrituración:
                - Notaria:
                - Impuesto:

            (Debes entregar solamente las variables solicitadas, es importante que mantengas el formato de la respuesta, ya que la respuesta que entregará el experto en estructurar información será llevada a una tabla y necesito que no tenga texto antes o después de la respuesta, solo las variables solicitadas en el formato que te mostré anteriormente. Si no tienes información para alguna variable coloca un - en su casilla correspondiente, pero no la omitas. No puedes agregar información adicional a la solicitada, ni omitir variables. Siempre están todas las variables solicitadas.)
            Este es el texto que debes estructurar: """

            Mensajes_tab_ode.append({"role": "user", "content": prompt+text_ode})

            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_tab_ode
            )
            
            prompts=[prompt+text_ode]

            ode_tabulada=response['choices'][0]['message']['content']
            my_bar.progress(20, text=progress_text+":robot_face:"+ "20%")
            #Existe codeudor?
            def check_sequence(text, sequence):
                if sequence in text:
                    return True
                else:
                    return False

            exis_codeudor=check_sequence(text_ode, 'CODEUDOR')
            print(exis_codeudor)

            ## Verificamos que mandatario sea igual a codeudor
            ### Verificación de codeudor

            ### Identificar si codeudor es igual a mandatario
            # Define your variables here
            personalidad = "Eres un experto en analizar información y solamente respondes True o False, no puedes hacer otra respuesta que no sea esta."

            prompt = """Verifica si el nombre del Mandatario es igual o no, en caso de que sí coloca True, en caso contrario False a la del codeudor en la siguiente información: """



            openai.api_key = api_keyx
            Mensajes_tab_ode=mensaje("Tab_ode")
            Mensajes_tab_ode.append({"role": "user", "content": prompt+text_ode})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": personalidad},
                    {"role": "user", "content": prompt+res_muestra3_ode},
                    {"role": "assistant", "content": "True"},
                    {"role": "user", "content": prompt+res_muestra2_ode},
                    {"role": "assistant", "content": "False"},
                    {"role": "user", "content": prompt+ode_tabulada},
                ]
            )
            

            igualdad=response['choices'][0]['message']['content']
            price_per_token = 0.001	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            print("The cost of the query is:", cost_in_dollars, "dollars")

            evalu_cod_man=eval(igualdad)
            print(evalu_cod_man)

            def check_sequence(text, sequence):
                if sequence in text:
                    return True
                else:
                    return False
            fragmento_texto=extract_substring(text, "\n\nVIGESIMO QUINTO:","\n\nVIGESIMO SEPTIMO:")
            revision=check_sequence(fragmento_texto,"no asume ninguna responsabilidad en el pago de las obligaciones que su mandante contrae por el presente instrumento")

            if revision==True:
                eval_frase="-Contiene la frase: Sí"
            elif revision==False:
                eval_frase="-Contiene la frase: No"

            #####################Análisis Borrador ############################
            ### Encabezado
            import openai
            inicio="COMPARECEN:"
            fin="\n\nPRIMERO:"
            fragmento_texto_encabezado=extract_substring(text, inicio, fin)
            #print(fragmento_texto_encabezado)


            time.sleep(40)

            # Define your variables here
            personalidad = "Eres un asistente que entregará información sobre de la inmobiliaria y datos solicitados del deudor, no puedes responder en otro formato que no sea el solicitado. Adenás vale agregar que puede que existan datos de más de una inmobilaria, como puede que solamente haya una. Solo puedes responder con la información solicitada, no se acepta otra respuesta que sea con la información solicitada."
            contexto = "Introduce una pregunta: "
            conocimiento_previo = """Este documento es un contrato de mutuo hipotecario,
                en el cual una se busca el nombre de quien adquiere una propiedad mediante un préstamo otorgado por
                la empresa CREDITÚ Administradora de Mutuos Hipotecarios S.A. El contrato establece las condiciones y
                obligaciones tanto del deudor como del acreedor, incluyendo la declaración de que el deudor no está inscrito en
                el Registro Nacional de Deudores de Pensiones de Alimentos. También se menciona la entrega del inmueble al comprador y
                su conformidad con la misma. Responde de forma completa y clara a las peticiones. Toma el rol de un ejecutivo
                que está corroborando la información de este documento pdf.
                siempre transformas los números de palabras por números de verdad.


            A continuación te daré instrucciones adicionales para tu respuesta:
            No puedes inventar información, si no encuentras la información, coloca None en el campo correspondiente.
            Los datos Nacionalidad, Profesión y Estado Civil son solo datos para el deudor. Además la columna rut puede ser tanto rol único tributario como cedula nacional.
            En caso de haber más de una inmobilaria, considerar todos los nombres y rut de las inmobiliarias.
            """

            prompt = """Extrae la información en este formato:
            Inmobiliaria Vendedora:

            - Nombre: 
            - Rut: 

            Deudor:

            - Nombre: 
            - Cédula Nacional: 
            - Nacionalidad: 
            - Profesión: 
            - Estado Civil: 
            en el siguiente fragmento de texto: """+ fragmento_texto_encabezado

            Mensajes_encabezado_preliminar=mensaje("Encabezado")
            Mensajes_encabezado=Mensajes_encabezado_preliminar
            Mensajes_encabezado.append({"role": "user", "content": "Nombre y rut de la inmobiliaria vendedora, nombre, cedula nacional o rol tributario, nacionalidad, profesión, estado civil del deudor en el siguiente documento:"+fragmento_texto_encabezado})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages= Mensajes_encabezado
            )

            cost=0
            respuesta_general_borrador=response['choices'][0]['message']['content']
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            prompts.append(prompt)
            ### respuesta < 2,4 seg significa un error en la respuesta

            ### Título del proyecto
            fragmento_texto=extract_substring(text, "\n\nSEGUNDO:", "\n\nTERCERO:")
            muestra_1='Por el presente instrumento, las Inmobiliarias, debidamente representadas en la forma indicada en la comparecencia, vende, cede y transfiere a doña AURELIA CONSTANZA MADRID SILVA quien compra, acepta y adquiere para sí, el departamento número ciento tres guion K, ubicado en el piso primero del Edificio K, y el estacionamiento número ochenta y cuatro guion B del primer piso, ambos del Sector II del Condominio, con acceso por calle Los Sauces número dos mil quinientos veinte, de la comuna de Padre Hurtado, en adelante también el “Inmueble”. Se deja constancia que al Inmueble le corresponde el rol de avalúo fiscal número ciento treinta y nueve guion ciento veintisiete, comuna de Padre Hurtado. Se comprenden en la compraventa los derechos proporcionales que al Inmueble le corresponden en los bienes comunes, conforme a lo establecido en la Ley de Copropiedad Inmobiliaria y en el Reglamento de Copropiedad General. La Compradora autoriza desde ya y en forma irrevocable a la Vendedora y a sus sucesoras legales, para modificar, adicionar, complementar o rectificar todos los Reglamentos de Copropiedad del Condominio, facultándola para firmar todo tipo de documentos, sean éstos instrumentos públicos o privados, así como para comparecer con derecho a voz y voto en las Asambleas de Copropietarios, tanto ordinarias como extraordinarias, que sean necesarias para dichos efectos, y queda facultada, desde ya, para constituir todas las servidumbres que se requieran para la evacuación de aguas lluvias, aguas servidas, acueducto, limpieza de fachadas y todas las demás necesarias para el adecuado funcionamiento del Condominio y su desarrollo. De la misma manera, en este acto la Compradora ratifica todas y cada una de las facultades conferidas a las Inmobiliarias en los Reglamentos de Copropiedad Inmobiliaria del Condominio, no siendo necesaria su reproducción. Asimismo, la Compradora acepta y autoriza a la Vendedora a efectuar publicidad, mantener una sala de ventas y hacer uso de las dependencias comunes del Condominio con el objeto de enajenar todas y cada una de las unidades que sean de su propiedad. De la misma manera, reconoce y acepta la existencia de departamentos pilotos durante toda la venta del mencionado Condominio.'
            muestra_2='Por el presente instrumento, Inmobiliaria Sur Cincuenta y Dos SpA, representada en la forma indicada, vende, cede y transfiere a doña YERARDI PATRICIA FRIZ ARANCIBIA, quien compra, acepta y adquiere para sí, la Unidad Exclusiva correspondiente al Departamento Número doscientos siete piso dos del Torre Número Tres, de una superficie edificada de cuarenta y seis coma sesenta y cuatro metros cuadrados, cuyo pre-rol del Servicio de Impuestos Internos es el número cuatro mil quinientos setenta guion ciento setenta y nueve; del Condominio Bosques de San Bernardo I, con dirección municipal y acceso por calle Camino La Vara cero dos mil seiscientos, comuna de San Bernardo, Región Metropolitana. Se comprende en lo vendido, la cuota proporcional sobre los bienes que se reputan comunes, inherentes e indivisibles con el dominio de la unidad que se transfiere, conforme a las disposiciones de la ley veintiún mil cuatrocientos cuarenta y dos, su reglamento y el Reglamento de Copropiedad Inmobiliaria.'

            #print(fragmento_texto)
            import openai

            # Define your variables here
            personalidad = "Eres un asistente que entregará información sobre de la inmobiliaria, representante de la inmobiliaria y datos solicitados del deudor"
            conocimiento_previo = """Este documento es un contrato de mutuo hipotecario,
                en el cual una se busca el nombre de quien adquiere una propiedad mediante un préstamo otorgado por
                la empresa CREDITÚ Administradora de Mutuos Hipotecarios S.A. El contrato establece las condiciones y
                obligaciones tanto del deudor como del acreedor, incluyendo la declaración de que el deudor no está inscrito en
                el Registro Nacional de Deudores de Pensiones de Alimentos. También se menciona la entrega del inmueble al comprador y
                su conformidad con la misma. Responde de forma completa y clara a las peticiones. Toma el rol de un ejecutivo
                que está corroborando la información de este documento pdf."""

            prompt = "Dame el nombre del proyecto del siguiente fragmento de texto: "

            Mensajes_tit_proyecto_preliminar=mensaje("Nombre del Proyecto:")
            Mensajes_tit_proyecto=Mensajes_tit_proyecto_preliminar
            Mensajes_tit_proyecto.append({"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_tit_proyecto
            )

            data_string=response['choices'][0]['message']['content']
            prompts.append(prompt+fragmento_texto)
            respuesta_general_borrador=respuesta_general_borrador + '\n\nNombre del Proyecto: \n\n' + data_string
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            ### Datos del inmueble
            import re
            my_bar.progress(30, text=progress_text+":robot_face:"+ "30%")
            def extract_substring_2(text):
                pattern = r"\n\n[A-Z]"
                matches = re.finditer(pattern, text)
                last_match = None
                second_last_match = None
                antepenultimate_match = None
                for match in matches:
                    antepenultimate_match = second_last_match
                    second_last_match = last_match
                    last_match = match
                if antepenultimate_match:
                    start_index = antepenultimate_match.start() + 2
                    end_index = text.find(":", start_index)
                    substring = text[start_index:end_index]
                    return substring
                else:
                    return ""

            # Example usage:
            result = extract_substring_2(text)
            print(result)
            ### Datos del inmueble
            fragmento_texto=extract_substring(text, "\n\nSEGUNDO:","\n\nTERCERO:")
            prompt = """Extrae los datos del inmuebles en este formato

-Número:  
-Torre:  
-Dirección: 
-Rol: 
-Lote: En caso de no encontrar el dato coloca un guion (-)
-Manzana: En caso de no encontrar el dato coloca un guion (-) y puede ser el piso del inmueble
No puedes extraer más que estos datos solicitados. Además el dato de la Manzana es puede ser el piso del inmueble.
Extrae esta información del siguiente fragmento de texto: """

            Mensajes_datos_inmueble_preliminar=mensaje("Datos del inmueble:")
            Mensajes_datos_inmueble=Mensajes_datos_inmueble_preliminar
            Mensajes_datos_inmueble.append( {"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_datos_inmueble
            )

            data_string=response['choices'][0]['message']['content']
            prompts.append(prompt+fragmento_texto)
            respuesta_general_borrador=respuesta_general_borrador + '\n\nDatos del inmueble: \n\n' + data_string
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            ### Datos del crédito (C3)
            fragmento_texto=extract_substring(text, "\n\nTERCERO:","\n\nCUARTO:")
            prompt = """Extrae los datos del crédito hipotecario:

            -Precio venta:
            -Monto líquido:
            -Monto bruto:
            -Gastos operacionales del préstamo:
            -Cuota contado: (inciso d) )
            - Precio venta estacionamiento: (Si no se encuentra el dato colocar un -)
            - Precio tasación estacionamiento: (Si no se encuentra el dato colocar un -)
            - Precio venta bodega: (Si no se encuentra el dato colocar un -)
            - Precio tasación bodega: (Si no se encuentra el dato colocar un -)

            Desglose Subsidio:
            - Tipo de subsidio:
            - Subsidio base:
            - Subsidio integración:
            - Subsidio captación:
            - Monto total subsidio:
            - Ahorro previo:

            del siguiente fragmento de texto: """

            Mensajes_dat_cred_3_preliminar=mensaje("Datos del Credito:")
            Mensajes_dat_cred_3=Mensajes_dat_cred_3_preliminar
            Mensajes_dat_cred_3.append({"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx
            time.sleep(20)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_dat_cred_3
            )
            data_string=response['choices'][0]['message']['content']
            prompts.append(prompt+fragmento_texto)
            respuesta_general_borrador=respuesta_general_borrador +"\n\n"+"Datos del Crédito: "+"\n\n" +data_string
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            ### Datos del crédito (C8)
            def buscar_banco(fragmento_texto):
                banco_alzante = "BANCO" in fragmento_texto
                return banco_alzante

            fragmento_texto=extract_substring(text, "\n\nOCTAVO:","\n\nNOVENO:")
            prompt = """Extrae los datos de un crédito hipotecario en el siguiente formato:  
-Monto líquido: 
-Monto bruto: 
-Gastos operacionales del préstamo: 

del siguiente fragmento de texto: """

            Mensajes_dat_cred_8_preliminar=mensaje("* -Monto líquido")
            Mensajes_dat_cred_8=Mensajes_dat_cred_8_preliminar
            Mensajes_dat_cred_8.append({"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_dat_cred_8
            )
            data_string=response['choices'][0]['message']['content']
            data_string = "*" + data_string

            prompts.append(prompt+fragmento_texto)
            respuesta_general_borrador=respuesta_general_borrador +"\n"+data_string
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            ### Datos del crédito (c9)
            import time
            my_bar.progress(40, text=progress_text+":robot_face:"+ "40%")
            time.sleep(60)
            fragmento_texto=extract_substring(text, "\n\nNOVENO:","\n\nDECIMO:")
            prompt = """Extrae los datos de un crédito en este formato:
- Plazo del crédito: 
- Meses de gracia: 
- Cuota dividendo sin seguro:
  - Cuota inicial:
  - Cuota final:
- Tasa del crédito: 
del siguiente texto: """

            Mensaje_dat_cred_9_preliminar=mensaje("- Plazo del crédito:")
            Mensaje_dat_cred_9=Mensaje_dat_cred_9_preliminar
            Mensaje_dat_cred_9.append({"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensaje_dat_cred_9
            )
            data_string=response['choices'][0]['message']['content']
            prompts.append(prompt+fragmento_texto)
            respuesta_general_borrador=respuesta_general_borrador + '\n\n' + data_string
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            ### Datos del mandatario
            fragmento_texto=extract_substring(text, "\n\nVIGESIMO QUINTO:","\n\nVIGESIMO SEPTIMO:")
            prompt = """Extrae la información de:
            Datos mandatario:
            -Nombre:
            -Rut:
            -Estado civil:
            -Profesión:
            -Dirección:
            (Solamente responde con las variables solicitadas sin omitir ninguna y no coloques texto antes ni después de las variables respondidas)
            del siguiente fragmento de texto:"""


            Mensajes_datos_mandatario_preliminar=mensaje("Datos Mandatario:")
            Mensajes_datos_mandatario=Mensajes_datos_mandatario_preliminar
            Mensajes_datos_mandatario.append({"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_datos_mandatario
            )

            data_string=response['choices'][0]['message']['content']
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            print("The cost of the query is:", cost_in_dollars, "dollars")
            respuesta_general_borrador=respuesta_general_borrador + '\n\n' +"Datos Mandatario:" +"\n\n"+ data_string
            prompts.append(prompt+fragmento_texto)
            ### Datos Codeudor
            #Extrae clausulas últimas
            def extract_finales_2(text, start=":", end=":", occurrence=1):
                end_index = len(text)
                for _ in range(occurrence):
                    end_index = text.rfind(end, 0, end_index)
                    if end_index == -1:  # No se encontró la secuencia final
                        return ""
                start_index = text.rfind(start, 0, end_index)
                if start_index == -1:  # No se encontró la secuencia de inicio
                    return ""
                start_index += len(start)

                # Check if "expone:" precedes the start index
                if start_index >= 7 and text[start_index-7:start_index] == "expone:":
                    while start_index >= 0 and text[start_index] != ".":


                        start_index -= 1
                    start_index += 1

                return text[start_index:end_index].strip()
            #Extracción clausula de codeudor

            prueba_text=text
            num_extra=0
            número_secuencia = 4

            clau_final = extract_finales_2(prueba_text, ":", ":", número_secuencia)
            if len(clau_final) <= 30:
                num_extra= 1
            clau_final = extract_finales_2(prueba_text, ":", ":", número_secuencia + num_extra)
            #   print("llegué acá ")

            número_secuencia = 6

            clau_final_extra = extract_finales_2(prueba_text, ":", ":", número_secuencia + num_extra)
            ### Extracción de datos
            ##Clausula 27
            clau_27=extract_substring(text, "\n\nVIGESIMO SEPTIMO:","\n\nVIGESIMO OCTAVO:")
            fragmento_texto="En este fragmento se encuentra, nombre, rut y dirección del codeudor:"+clau_final + "\n" +"Y en el texto que viene a continuación se encuentra el estado civil de codeudor:" +"\n"+clau_final_extra	 + "Puede que en este fragmento haya información adicional de la solicitada: " + clau_27
            personalidad = "Eres un experto en analizar la información solicitada de un fragmento de texto. Nunca respondes los números con palabras. "

            prompt = """Extrae la información de:
            Datos Codeudor:
            -Nombre:
            -Rut: (Si no se encuentra el dato colocar un -)
            -Estado civil:
            -Dirección: (Si no se encuentra el dato colocar un -)
            (Solamente responde con las variables solicitadas sin omitir ninguna y no coloques texto antes ni después de las variables respondidas)
            del siguiente fragmento de texto:"""
            my_bar.progress(60, text=progress_text+":robot_face:"+ "60%")
            Mensajes_codeudor_preliminar=mensaje("Datos Codeudor:")
            Mensajes_codeudor=Mensajes_codeudor_preliminar
            Mensajes_codeudor.append({"role": "user", "content": prompt+fragmento_texto})
            if exis_codeudor == True:
                if evalu_cod_man== False:



                    openai.api_key = api_keyx

                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo-0125",
                        messages=Mensajes_codeudor
                    )

                    data_string=response['choices'][0]['message']['content']
                    price_per_token = 0.0005 	  # Replace with the actual price per token
                    total_tokens = response['usage']['total_tokens']
                    cost_in_dollars = price_per_token * total_tokens/1000
                    cost= cost+cost_in_dollars
                    respuesta_general_borrador=respuesta_general_borrador + '\n\n' +"Datos Codeudor:" +"\n\n"+ data_string
                elif evalu_cod_man== True:
                    respuesta_general_borrador=respuesta_general_borrador + '\n\n' +"Datos Codeudor:" +"\n\n"+ data_string
            elif exis_codeudor == False:
                data_string="""
            Datos Codeudor:
            -Nombre: -
            -Rut: -
            -Estado civil: -
            -Dirección: -
            """
                respuesta_general_borrador=respuesta_general_borrador + '\n\n' +"Datos Codeudor:" +"\n\n"+ data_string
            ### Gastos operacionales
            fragmento_texto=extract_substring(text, "\n\nTRIGESIMO:","\n\nTRIGESIMO PRIMERO:")
            Mensajes_GOP_preliminar=mensaje("Gastos Operacionales:")
            Mensajes_GOP=Mensajes_GOP_preliminar
            prompt = """Extrae la información de:
Gastos Operacionales:
- Tasación:
- Estudio de Títulos:
- Notaría en Santiago:
- Redacción de escritura:
- Impuesto Mutuo: (se encuentra en literal f) )
- CBR: (Conservador de bienes raíces)

(Solamente responde con las variables solicitadas sin omitir ninguna y no coloques texto antes ni después de las variables respondidas)
del siguiente fragmento de texto:"""
            Mensajes_GOP.append({"role": "user", "content": prompt+fragmento_texto})
            openai.api_key = api_keyx

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=Mensajes_GOP
            )

            data_string=response['choices'][0]['message']['content']
            price_per_token = 0.0005 	  # Replace with the actual price per token
            total_tokens = response['usage']['total_tokens']
            cost_in_dollars = price_per_token * total_tokens/1000
            cost= cost+cost_in_dollars
            respuesta_general_borrador=respuesta_general_borrador + '\n\n' +"Gastos Operacionales:"+'\n\n' +data_string
            prompts.append(prompt+fragmento_texto)
            ### Banco alzante
            fragmento_texto=extract_substring(text, "\n\nOCTAVO:","\n\nNOVENO:")
            banco_alzante=buscar_banco(fragmento_texto)
            prompt = """Extrae la información de:
            Banco:
            -Nombre:
            """
            Mensajes_Banco_alzante_preliminar=mensaje("Banco:")
            Mensajes_Banco_alzante=Mensajes_Banco_alzante_preliminar
            Mensajes_Banco_alzante.append({"role": "user", "content": prompt+fragmento_texto})
            if banco_alzante==True:
            


                prompt = """Extrae la información de:
                Banco:
                -Nombre:
                """


                openai.api_key = api_keyx

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo-0125",
                    messages=Mensajes_Banco_alzante
                )
        
                data_string=response['choices'][0]['message']['content']
                price_per_token = 0.0005 	  # Replace with the actual price per token
                total_tokens = response['usage']['total_tokens']
                cost_in_dollars = price_per_token * total_tokens/1000
                cost= cost+cost_in_dollars
                respuesta_general_borrador=respuesta_general_borrador + '\n\n' + data_string
                prompts.append(prompt+fragmento_texto)
            my_bar.progress(90, text=progress_text+":robot_face:"+ "90%")
            ### Comparacion de datos
            prompt="Necesito que compares los siguientes datos uno es un borrador el cual corresponde a: "+respuesta_general_borrador+"\n\n"+" y el otro documento corresponde a ODE y corresponde a:"+"\n\n" +ode_tabulada+" \n, por favor compara los datos y entrega la información en formato de tabla csv."
            openai.api_key = api_keyx


            Mensajes_comparacion=mensaje("Comparacion")
            Mensajes_comparacion.append({"role": "user", "content":prompt})
            response = openai.ChatCompletion.create(
                model="gpt-4-0125-preview",
                messages=Mensajes_comparacion


            )
            end_time = time.time()
            execution_time = end_time - start_time
            comparacion=response['choices'][0]['message']['content']
            prompts.append(prompt)
            #df = pd.read_csv(StringIO(comparacion),delimiter=";")
            
            #st.write(comparacion)
            my_bar.progress(100, text=progress_text+":robot_face:"+ "Listo!")
            time.sleep(2)
            # Crear un DataFrame desde la cadena de texto
            df_comparacion = pd.read_csv(StringIO(comparacion),delimiter=";")
            print(df_comparacion)
            end_time = time.time()  # Guarda el tiempo actual después de ejecutar el script

            execution_time = end_time - start_time  # Calcula la diferencia entre los dos tiempos

            print(f"El script tardó {execution_time} segundos en ejecutarse.")


            my_bar.empty()
            
            # Mostrar resultados
            st.header("Resultados")
            st.write(f"El script tardó {execution_time} segundos en ejecutarse.")
            st.write(f"El costo de ejecución fue de {cost} dólares.")
            # Aplicar estilo condicional
            
            def color_comparacion(val):
                    if val == 'IGUAL':
                        return 'background-color: green; color: white'
                    elif val == 'NO IGUAL':
                        return 'background-color: red; color: white'
                    else:
                        return ''
            # Aplicar estilo condicional
            st.write("Comparación de datos")
            st.dataframe(df_comparacion.style.applymap(color_comparacion))
            #st.dataframe(df_comparacion)
            

            import os
            import random
            id = random.randint(10000, 99999)




            ### Guardando en registro
            path_registro=r"C:\Users\cgomez\Desktop\Proyectos\Automatización_de_procesos\Registro"

            
            
            # Crear la carpeta dentro del directorio path_registro
            
            #carpeta= rut_cliente+"_"+ejecutivo+"_"+str(id)
            #st.write("Tu código de operación es: ")
            #Path = f'''{carpeta}'''
            #st.code(Path, language="python")

            ruta_carpeta="Pag_web/Registros"
    
            # Verificar si la carpeta se creó exitosamente
            if os.path.exists(ruta_carpeta):
                print("Carpeta creada exitosamente en:", ruta_carpeta)
            else:
                print("Error al crear la carpeta de registro.")
                
            #Respuesta_general_borrador
            path = ruta_carpeta +"/"+"respuesta_general_borrador.txt"
            with open(path, "w") as file:
                file.write(respuesta_general_borrador)
                #Respuesta_general_borrador
            path = ruta_carpeta +"/"+"ODE_formato_analisis.txt"
            with open(path, "w") as file:
                file.write(ode_tabulada)
            path = ruta_carpeta +"/"+"Nombre_de_Operador.txt"
            st.write("El nombre del operador es: ", ejecutivo)
            with open(path, "w") as file:
                file.write(ejecutivo)
            path = ruta_carpeta +"/"+"comparacion.csv"
            df_comparacion.to_csv(path, index=False, sep=";")
            print("Iniciando proceso de envío de registros")
            CLIENT_SECRET_FILE = "Pag_web/correo.json"
            SERVICE_ACCOUNT_FILE = "Pag_web/client_secret.json"
            API_NAME = "drive"
            API_VERSION = "v3"
            SCOPES = ["https://www.googleapis.com/auth/drive"]
            ruta_carpeta="Pag_web/Registros"
            ###Ejecutivo

            ### Rut
            rut=df_comparacion[df_comparacion["Puntos"]=="Cédula Nacional"]["Dato ODE"]
            inde=rut.index[0]
            rut=rut[inde]
            ### código único
            codigo = str(random.randint(10000, 99999))

            ### Nombre carpeta
            carpeta=ejecutivo+"_"+rut+"_"+codigo

            service = Create_Service_With_Service_Account(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
            #service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
            # Crear una carpeta en Google Drive
            parent_folder_id = '1bqJrjgUHaz4dI2NYNIgEC_6ixNPkbjQG'

            folder_metadata = {
            'name': carpeta,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_folder_id]  # Aquí se especifica la carpeta padre
            }
            print("Creando carpeta en Google Drive")
            folder = service.files().create(body=folder_metadata, fields='id').execute()
            folder_id = folder.get('id')
            time.sleep(5)
            path_borrador = ruta_carpeta +"/"+"respuesta_general_borrador.txt"
            path_ode = ruta_carpeta +"/"+"ODE_formato_analisis.txt"
            ejecutivo_path=ruta_carpeta+"/"+"Nombre_de_Operador.txt"
            comparacion_ruta=ruta_carpeta+"/"+"comparacion.csv"
            file_names = [path_borrador, path_ode, ejecutivo_path,comparacion_ruta]
            mime_types = ["text/plain", "text/plain", "text/plain", "text/csv"]
            count=0
            for file_name, mime_type in zip(file_names, mime_types):
                file_metadata = {
                    "name" : os.path.basename(file_name),
                    "parents" : [folder_id]
                }

                media = MediaFileUpload(file_name, mimetype=mime_type)

                file = service.files().create(
                    body=file_metadata,
                    media_body = media,
                    fields = "id"
                ).execute()
                if count==3:
                    id_comparacion = file.get('id')
                elif count==2:
                    id_ejecutivo = file.get('id')
                count+=1

            st.write("Tu código de operación es: ")
            id_operacion="["+"'"+id_comparacion+"'"+","+"'"+id_ejecutivo+"'"+","+"'"+folder_id+"'"+"]"
            st.code(id_operacion, language="python")

            import subprocess

            # Ruta al archivo .py que quieres ejecutar
            
            
        else:
            st.warning("Por favor, carga ambos documentos antes de ejecutar el código.")



if __name__ == "__main__":
    main()

