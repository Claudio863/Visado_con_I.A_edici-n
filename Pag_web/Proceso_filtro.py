# Aquí puedes agregar el código que deseas ejecutar con los documentos cargados
# Utiliza doc1 y doc2 para acceder a los contenidos de los documentos
#progress_text = "Comparando documentos...   "
#my_bar = st.progress(0, text=progress_text)
import time
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
import nltk
import re

# Descargar las stopwords de NLTK
nltk.download('stopwords')

import openai
import os
import streamlit as st

from PIL import Image

def proceso (text,Entrenam,ode_path):
    import time
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
    import nltk
    import re

    # Descargar las stopwords de NLTK
    nltk.download('stopwords')

    import openai
    import os
    import streamlit as st

    from PIL import Image
    
    progress_text = "Comparando el documento..."
    my_bar = st.progress(0, text=progress_text)
    my_bar.progress(0, text=progress_text+":robot_face:"+ "0%")
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
        s_lower = s.lower()
        start_lower = start.lower()
        end_lower = end.lower()
        
        start_index = s_lower.find(start_lower)
        if start_index == -1:  # La secuencia de inicio no se encontró
            return None
        start_index += len(start)  # Mover el índice de inicio al final de la secuencia de inicio

        end_index = s_lower.find(end_lower, start_index)
        if end_index == -1:  # La secuencia de final no se encontró
            return None
        
        return s[start_index:end_index]
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
    import re

    ## Función que permite extraer fragmento independiente de si es una palabra o una secuencia de palabras
    def extract_substring(s, start, end):
        s_lower = s.lower()
        start_lower = start.lower()
        end_lower = end.lower()
        
        start_index = s_lower.find(start_lower)
        if start_index == -1:  # La secuencia de inicio no se encontró
            return None
        start_index += len(start)  # Mover el índice de inicio al final de la secuencia de inicio

        end_index = s_lower.find(end_lower, start_index)
        if end_index == -1:  # La secuencia de final no se encontró
            return None
        
        return s[start_index:end_index]

    #####################################################Realizar for para cada carpeta fine-tunning



    from nltk.corpus import stopwords

    def remove_stopwords_and_numbers(texto):
        # Obtener las stopwords en español
        stop_words = set(stopwords.words('spanish'))
        
        # Eliminar los números
        texto = re.sub(r'\d+', '', texto)
        
        # Tokenizar el texto en palabras
        words = texto.split()
        
        # Filtrar las palabras que no son stopwords
        filtered_words = [word for word in words if word.lower() not in stop_words]
        
        # Unir las palabras filtradas en una cadena de texto nuevamente
        filtered_text = ' '.join(filtered_words)
        
        return filtered_text

    # Aplicar la función a la variable 'text'
    texto = remove_stopwords_and_numbers(text)

    print(texto)
    text_ode = leer_pdf(ode_path)
        # Imprimir el contenido
        # print(text)

    ### Tabulación ODE
    #(Marketing)
    api_keyx=st.secrets["API_KEY_OPENAI"]
    #(Operaciones)
    #api_keyx="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"

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
    #my_bar.progress(20, text=progress_text+":robot_face:"+ "50%")
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


    #####################Análisis Borrador ############################
    ### Encabezado
    import openai
    inicio="compraventa"
    fin="PRIMERO:"
    fragmento_texto_encabezado=extract_substring(texto, inicio, fin)
    #print(fragmento_texto_encabezado)


    time.sleep(20)
    my_bar.progress(30, text=progress_text+":robot_face:"+ "30%")
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
    fragmento_texto=extract_substring(texto, "SEGUNDO:", "TERCERO:")
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
    result = extract_substring_2(texto)
    print(result)
    ### Datos del inmueble
    fragmento_texto=extract_substring(texto, "SEGUNDO:","TERCERO:")
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
    fragmento_texto=extract_substring(texto, "TERCERO:","CUARTO:")
    prompt = """Extrae los datos del crédito hipotecario:

    -Precio venta:
    -Monto líquido:
    -Monto bruto:
    -Gastos operacionales del préstamo:
    -Cuota contado:
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
    my_bar.progress(60, text=progress_text+":robot_face:"+ "60%")

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

    fragmento_texto=extract_substring(texto, "OCTAVO:","NOVENO:")
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

    time.sleep(40)
    fragmento_texto=extract_substring(texto, "NOVENO:","DECIMO:")
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
    my_bar.progress(80, text=progress_text+":robot_face:"+ "80%")

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
    fragmento_texto=extract_substring(texto, "VIGESIMO QUINTO:","VIGESIMO SEPTIMO:")
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
    clau_27=extract_substring(texto, "VIGESIMO SEPTIMO:","VIGESIMO OCTAVO:")
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
    fragmento_texto=extract_substring(texto, "TRIGESIMO:","TRIGESIMO PRIMERO:")
    Mensajes_GOP_preliminar=mensaje("Gastos Operacionales:")
    Mensajes_GOP=Mensajes_GOP_preliminar
    prompt = """Extrae la información de:
    Gastos Operacionales:
    - Tasación:
    - Estudio de Títulos:
    - Notaría en Santiago:
    - Redacción de escritura:
    - Impuesto Mutuo: (se encuentra en literal f) )
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
    fragmento_texto=extract_substring(texto, "OCTAVO:","NOVENO:")
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

    ### Comparacion de datos
    prompt="Necesito que compares los siguientes datos uno es un borrador el cual corresponde a: "+respuesta_general_borrador+" y el otro documento corresponde a ODE y corresponde a:" +ode_tabulada+" \n, por favor compara los datos y entrega la información en formato de tabla csv."
    openai.api_key = api_keyx
    my_bar.progress(90, text=progress_text+":robot_face:"+ "90%")


    Mensajes_comparacion=mensaje("Comparacion")
    Mensajes_comparacion.append({"role": "user", "content":prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=Mensajes_comparacion


    )
    comparacion=response['choices'][0]['message']['content']
    prompts.append(prompt)
    try:
        df = pd.read_csv(StringIO(comparacion),delimiter=";")
    except:
        Mensajes_comparacion=mensaje("Comparacion")
        Mensajes_comparacion.append({"role": "user", "content":prompt})
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",
            messages=Mensajes_comparacion)
        df = pd.read_csv(StringIO(comparacion),delimiter=";")
    my_bar.progress(100, text=progress_text+":robot_face:"+ "100%")
    return(df, respuesta_general_borrador, cost, prompts, ode_tabulada)
