
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Pag_web/client_secret.json'
# pip install google-cloud-documentai
from google.cloud import documentai
from google.api_core.client_options import ClientOptions

import os
import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
endpoint = 'documentai.googleapis.com'
location='us'
project_id="appvisado"
processor_id="f4abc41069d62d01"

def get_text_from_pdf_ocr(file_path):
    try:
        mime_type = 'application/pdf'
        client = documentai.DocumentProcessorServiceClient(
            client_options=ClientOptions(api_endpoint=f"{location}-{endpoint}"))
        name = client.processor_path(project_id, location, processor_id)
        with open(file_path, "rb") as image:
            image_content = image.read()
        
        raw_document = documentai.RawDocument(
            content=image_content, mime_type=mime_type)
        
        request = documentai.ProcessRequest(name=name, raw_document=raw_document)
        response = client.process_document(request=request)
        document = response.document
        return document.text
    except Exception as e:
        st.write(e)
        return None

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



