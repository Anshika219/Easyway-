from fastapi import FastAPI, Form, File, UploadFile
from backend.llm_part import extract_expense
from backend.ocr_part import extract_text_from_image

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/parse-expense")
def parse_expense(
    text: str = Form(None),
    file: UploadFile = File(None)
):
    if file is not None:
        image_bytes = file.file.read()
        ocr_text = extract_text_from_image(image_bytes)
        result = extract_expense(ocr_text)
        return result

    if text is not None:
        result = extract_expense(text)
        return result

    return {
        "amount": 0,
        "merchant": "Unknown",
        "category": "Other",
        "date": "Unknown",
        "payment_mode": "Unknown",
        "confidence": 0.0,
        "reasoning": "No input provided"
    }
