from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = "correo.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

ruta_carpeta="Pag_web/Registros"
path_borrador = ruta_carpeta +"/"+"respuesta_general_borrador.txt"
path_ode = ruta_carpeta +"/"+"ODE_formato_analisis.txt"
ejecutivo=ruta_carpeta+"/"+"Nombre_de_Operador.txt"
comparacion=ruta_carpeta +"/"+"comparacion.csv"

folder_id = "1rthen8yATgfMEdM0K3ZocYYc8u_zTaaC"
file_names = [path_borrador, path_ode, ejecutivo,comparacion]
mime_types = ["text/plain", "text/plain", "text/plain", "text/csv"]

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name" : file_name,
        "parents" : [folder_id]
    }

    media = MediaFileUpload("./Drive/{0}".format(file_name), mimetype=mime_type)

    service.files().create(
        body=file_metadata,
        media_body = media,
        fields = "id"
    ).execute()
    
