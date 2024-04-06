import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import random
import time 
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


CLIENT_SECRET_FILE = "Pag_web/correo.json"
SERVICE_ACCOUNT_FILE = "Pag_web/Cred.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]
# List all files in the specified folder

service = Create_Service_With_Service_Account(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
# Read the TSV file from Google Drive
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
for operador in df["Operador"]:
    st.write(operador)
    id_operacion=df[df["Operador"]==operador]["ID"]
    inde=id_operacion.index[0]
    id_operacion=id_operacion[inde]
    st.code(id_operacion, language="python")
# Read the CSV file
# File uploader
id_comparacion=st.text_input("Introduzca código de la operación para la revisión")
#st.write(len(carpeta)) 


if len(id_comparacion) is not 0:
    #st.write(type(id_comparacion))
    ids=eval(id_comparacion)
    for id in range(len(ids)):
        if id==0:
            comparacion_id=ids[id]
        elif id==1:
            ejecutivo_id=ids[id]
        elif id==2:
            F_T_carpeta_id=ids[id]
    #st.write(comparacion_id)
    ## Abriendo el archivo id
    

    service = Create_Service_With_Service_Account(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
    #st.write(comparacion_id[0])
    file_ids = [comparacion_id, ejecutivo_id]
    file_names = ["comparacion.csv","Nombre_de_Operador.txt"]

    # Download files from Google Drive
    for file_id, file_name in zip(file_ids, file_names):
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        fh.seek(0)
        if file_name.endswith('.csv'):
            df_comparacion = pd.read_csv(fh, delimiter=";", encoding="utf-8")
            # Do something with the CSV file
        else:
            ejecutivo = fh.read().decode('utf-8')
            # Do something with the string file
    #st.dataframe(df_comparacion)
    
    # Store the DataFrame in the session state

    #st.dataframe(df)

    # Add a checkbox column

    def color_comparacion(val):
        if val == 'IGUAL':
            return 'background-color: green; color: white'
        elif val == 'NO IGUAL':
            return 'background-color: red; color: white'
        else:
            return ''

    df_comparacion['dato_corr_borrador'] = False
    df_comparacion['dato_corr_ode'] = False
    df_comparacion['corrección_comparacion'] = False
    df_comparacion['Correccioneas_borrador']=False
    #st.dataframe(df_comparacion)
    for indice in range(len(df_comparacion)):
        df_comparacion["Correccioneas_borrador"][indice]="Sin correcciones"
    df_comparacion = df_comparacion.style.applymap(color_comparacion, subset=['Comparación'])

    df_comparacion_editado=st.data_editor(
        df_comparacion,
            column_config={
                "dato_corr_ode": st.column_config.CheckboxColumn(
                label="Extrajo incorrectamente dato ODE",
                help="Selecciona lo que está correcto con la ODE",
                default=False),
                            
                "corrección_comparacion": st.column_config.CheckboxColumn(
                label="Comparó incorrectamente los datos",
                help="Selecciona lo que está correcto del borrador con la ODE original",
                            default=False,
                        ),
                "dato_corr_borrador": st.column_config.CheckboxColumn(
                label="Extrajo incorrectamente dato Borrador",
                help="Selecciona lo que está correcto del borrador con la ODE original",
                    default=False,
                ),
                            "Correccioneas_borrador": st.column_config.Column(
                label="Dato mal redactado en el borrador",
                help="Comenta el dato que está mal redactado en el borrador", 
                    required=True,
                ),
                

                "Puntos": st.column_config.Column(
                label="Puntos",
                help="En esta sección debes editar en el caso de que sea necesario",
                required=True,

                ),
                "Dato Borrador": st.column_config.Column(
                    "Dato Borrador",
                    help="En esta sección debes editar en el caso de que sea necesario",
                    required=True,

                ),
                "Dato ODE": st.column_config.Column(
                    "Dato ODE",
                    help="En esta sección debes editar en el caso de que sea necesario",
                    required=True,
                        
                    )

                        },
                    
                    disabled=["Comparación"],
                    hide_index=True,
                )


    #st.dataframe(st.session_state.df)


    #print(df_comparacion_editado.data)
    if st.button("Guardar"):
        ruta_carpeta="/mount/src/visado_con_i.a/Pag_web/Registros"
        df_comparacion_editado_SE=df_comparacion_editado.values
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
        import pandas as pd
        from reportlab.lib.styles import getSampleStyleSheet
        import datetime
        ###Análisis df_comparacion_editado
        
        correcciones=[]
        # Create a copy of the DataFrame to avoid modifying it while iterating
        df_comparacion_editado_copy = df_comparacion_editado.copy()

        for i in range(len(df_comparacion_editado["Comparación"])):
            try:
                if df_comparacion_editado["corrección_comparacion"][i] == True and df_comparacion_editado["Comparación"][i] == "IGUAL":
                    df_comparacion_editado_copy["Comparación"][i] = "NO IGUAL"

                elif df_comparacion_editado["corrección_comparacion"][i] == True and df_comparacion_editado["Comparación"][i] == "NO IGUAL":
                    df_comparacion_editado_copy["Comparación"][i] = "IGUAL"
                if df_comparacion_editado["Correccioneas_borrador"][i] != "Sin correcciones":
                    correcciones.append(df_comparacion_editado["Correccioneas_borrador"][i])
            except:
                continue
        # Replace the original DataFrame with the modified copy
        df_comparacion_editado = df_comparacion_editado_copy
        ruta_feed= ruta_carpeta+"/"+"comparacion_feed.csv"
        df_comparacion_editado.to_csv(ruta_feed, sep=";", index=False, encoding="utf-8")
        num_errores=0
        for valor in df_comparacion_editado_copy["Comparación"]:
            if valor == "NO IGUAL":
                num_errores+=1
        df_pdf = df_comparacion_editado.iloc[:, :4]
        # Convertir el DataFrame a una lista de listas
        data = [df_pdf.columns.tolist()] + df_pdf.values.tolist()
        styles = getSampleStyleSheet()
        ruta_carpeta="/mount/src/visado_con_i.a/Pag_web/Registros"
        # Crear el documento PDF
        pdf_filename = ruta_carpeta+"/"+"tabla.pdf"
        pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
        table = Table(data)
        ############ENCABEZADO
        header = Paragraph(f"Documento analizado por: {ejecutivo}", styles['Heading1'])
        # Estilo de la tabla
        # Define the table style without the problematic line
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 5),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ])

        # Create the table
        table = Table(data, style=style)

        # Set the background color of each cell based on the 'Comparación' column
        for i, val in enumerate(df_comparacion_editado['Comparación']):
            if val == 'IGUAL':
                table.setStyle(TableStyle([('BACKGROUND', (0, i+1), (-1, i+1), colors.green)]))
            else:
                table.setStyle(TableStyle([('BACKGROUND', (0, i+1), (-1, i+1), colors.red)]))
        correcciones_string=""
        count=0
        for correccion in correcciones:
            correcc=f"{count}.- {correccion}<br/>"
            correcciones_string=correcciones_string+correcc
            count+=1
        table.setStyle(style)
        Retroalimentacion = f"<b>Cantidad de Errores:</b> {num_errores}<br/><br/><b>Correcciones:</b><br/>{correcciones_string}"
        footer = Paragraph(Retroalimentacion, styles['Normal'])
        # Construir la tabla y agregarla al documento
        pdf.build([header, table, footer])

        # Guardar la figura en el archivo PDF
        path_feed= ruta_carpeta+"/"+"df_comparacion_feed.csv"
        df_comparacion_editado.to_csv(path_feed, sep=";", index=False, encoding="utf-8")
        st.success("Tabla guardada con éxito")
        contador=0
        print("Iniciando proceso de envío de registros")
        CLIENT_SECRET_FILE = "Pag_web/correo.json"
        SERVICE_ACCOUNT_FILE = "Pag_web/Cred.json"
        API_NAME = "drive"
        API_VERSION = "v3"
        SCOPES = ["https://www.googleapis.com/auth/drive"]
        ruta_carpeta="/mount/src/visado_con_i.a/Pag_web/Registros"
        ###Ejecutivo
        
        #ejecutivo="gabriel"
        

        ### Rut
        comparacion_ruta=ruta_carpeta +"/"+"comparacion.csv"
        comparacion=pd.read_csv(comparacion_ruta,delimiter=";",encoding="utf-8")
        nombre=comparacion["Dato ODE"][4]
        rut=comparacion[comparacion["Puntos"]=="Cédula Nacional"]["Dato ODE"]
        inde=rut.index[0]
        rut=rut[inde]
        ### código único
        codigo = str(random.randint(10000, 99999))

        ### Nombre carpeta
        fecha = datetime.datetime.now().strftime("%Y-%m-%d")
        registro=rut+"_"+nombre+"_"+codigo+"_"+fecha

        service = Create_Service_With_Service_Account(SERVICE_ACCOUNT_FILE, API_NAME, API_VERSION, SCOPES)
        #service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        # Crear una carpeta en Google Drive
        file_names = [pdf_filename, path_feed]
        mime_types = ["application/pdf", "text/csv"]
        count=0
        for file_name, mime_type in zip(file_names, mime_types):
            if count==1:
                folder_id = F_T_carpeta_id
                #st.write(folder_id)
                name="df_comparacion_feed.csv"
                file_metadata = {
                    "name" : name,
                    "parents" : [folder_id]
                }
            elif count==0:
                folder_id = "14j0supDzl_c7cct9ZwHALFAE5ziLq2Q-"
                name=registro+".pdf"
                file_metadata = {
                    "name" : name,
                    "parents" : [folder_id]
                }

            media = MediaFileUpload(file_name, mimetype=mime_type)

            service.files().create(
                body=file_metadata,
                media_body = media,
                fields = "id"
            ).execute()
            count+=1
        st.markdown("**Código de la operación:**")
        st.code(registro, language="python")
        st.markdown("**Observaciones:**")
        observaciones= correcciones_string.replace("<br/>", "\n")
        st.code(observaciones, language="python")
        #for correccion in range(len(df_comparacion["Correccioneas_borrador"])):
        #   if df_comparacion["Correccioneas_borrador"][correccion] != "Sin correcciones":
        #        st.write(f"{contador} .- {df_comparacion['Correccioneas_borrador'][correccion]}")
        #        contador+=1
