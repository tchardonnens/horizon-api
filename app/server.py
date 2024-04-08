import os
import sys
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
from PIL import Image
import tempfile

sys.path.append(os.path.dirname(__file__))

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")
    
    try:
        # Save temporary pdf file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            temp_pdf.write(await file.read())
            temp_pdf_path = temp_pdf.name
            print(temp_pdf_path)
        
        # Convert PDF to list of images
        images = convert_from_path(temp_pdf_path)
        
        # Perform OCR on each image
        ocr_results = [pytesseract.image_to_string(image) for image in images]
        
        # Combine OCR results
        combined_text = "\n".join(ocr_results)
        
        return {"text": combined_text}
    finally:
        # Clean up temporary file
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)