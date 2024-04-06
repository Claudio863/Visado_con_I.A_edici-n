# Ejecutar el archivo .py
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from Google import Create_Service_With_Service_Account
import pandas as pd
import random
import time
import streamlit as st 
import os
from googleapiclient.http import MediaIoBaseDownload
import io

print("Iniciando proceso de envío de registros")
def envio_registro_F_T(df_comparacion, ejecutivo, respuesta_general_borrador, ode_tabulada):

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
    SERVICE_ACCOUNT_FILE = "Pag_web/Cred.json"
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
    file_id = "1rP6YfD0fauut314c0c4dB3HmWJ-Ks-T8"
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    fh.seek(0)
    # Convert the TSV file to a DataFrame
    #st.write(downloader)
    df = pd.read_csv(fh, delimiter="\t")
    # Get the current index
    index = df.index.tolist()

    # Swap the second and third rows
    index[0], index[1], index[2] = index[1], index[2], index[0]

    # Reindex the DataFrame
    #df_nuevo = df.reindex(index)
    df = df.drop(df.index[0])
    df = df.reset_index(drop=True)
    from datetime import datetime

    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Extraer la hora y la fecha
    hora_actual = fecha_actual.strftime("%H:%M:%S")
    fecha_actual = fecha_actual.strftime("%Y-%m-%d")

    print("Hora actual:", hora_actual)
    print("Fecha actual:", fecha_actual)
    new_row = {'Operador': ejecutivo+"   Fecha:"+fecha_actual+", Hora:"+hora_actual, 'ID': id_operacion}
    df = pd.concat([df, pd.DataFrame(new_row, index=[0])], ignore_index=True)
    df.to_csv(ruta_carpeta+"/"+'Ultimos_registros.tsv', sep='\t', index=False)
    media = MediaFileUpload(ruta_carpeta+"/"+'Ultimos_registros.tsv', mimetype='text/tab-separated-values')
    # Update the file
    service.files().update(fileId=file_id, media_body=media).execute()
    return id_operacion
    