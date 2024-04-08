import os
import sys
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai import MistralAIEmbedding
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from llama_index.core.llms import ChatMessage
from pdf2image import convert_from_path
import pytesseract
import numpy as np
from numpy.linalg import norm
import tempfile
from pydantic import BaseModel
from app.xml_template import template_xml_without_values, template_xml_without_values_embedding

sys.path.append(os.path.dirname(__file__))

app = FastAPI()

class ScoreRequest(BaseModel):
    ocr_text: str
    llm_output: str

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(await file.read())
            temp_pdf_path = temp_pdf.name
            print(temp_pdf_path)
        
        images = convert_from_path(temp_pdf_path)
        
        ocr_results = [pytesseract.image_to_string(image) for image in images]
        
        combined_text = "\n".join(ocr_results)
        xml_generation_response = await generate_xml(combined_text)
        return {"text": combined_text, "xml": xml_generation_response}
    finally:
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)

@app.post("/generate-xml/")
async def generate_xml(text: str):
    messages = [
        ChatMessage(role="system", content=f'You are an expert in mapping municipal by-laws into xml files. YOU HAVE TO OUTPUT ONLY WITH THE FOLLWING TEMPLATE: {template_xml_without_values} use the values provide by the user'),
        ChatMessage(role="user", content=text),
    ]

    resp = MistralAI(api_key=os.environ.get('MISTRAL_API_KEY'), max_tokens=50000, temperature=0.1).chat(messages)
    return resp.message.content

@app.post("/score/")
async def score(request: ScoreRequest):
    embed_model = MistralAIEmbedding(model_name="mistral-embed", api_key=os.environ.get('MISTRAL_API_KEY'))

    output_text_embedding = embed_model.get_text_embedding(request.llm_output)
    ocr_text_embedding = embed_model.get_text_embedding(request.ocr_text)

    np_output_text_embedding = np.array(output_text_embedding)
    np_ocr_text_embedding = np.array(ocr_text_embedding)
    np_template_xml_embedding = np.array(template_xml_without_values_embedding)

    output_vector = np_output_text_embedding - np_template_xml_embedding

    cosine_similarity = np.dot(output_vector, np_ocr_text_embedding) / (norm(output_vector) * norm(np_ocr_text_embedding))

    return {"cosine_similarity": cosine_similarity}