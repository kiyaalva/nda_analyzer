from fastapi import FastAPI, UploadFile, File, HTTPException
from app.parsers.pdf_parser import extract_text_from_pdf
from app.parsers.docx_parser import extract_text_from_docx
from app.services.analyzer import analyze_contract_text
import tempfile, os

app = FastAPI(title="NDA Analyzer API")

@app.get("/health")
async def health():
    return {"status":"ok"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    ext = (file.filename or "").lower()
    content = await file.read()
    text = ""

    if ext.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        try:
            text = extract_text_from_pdf(tmp_path)
        finally:
            os.remove(tmp_path)
    elif ext.endswith(".docx"):
        text = extract_text_from_docx(content)
    else:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX supported in v1")

    if not text.strip():
        raise HTTPException(status_code=422, detail="Could not extract text")

    result = await analyze_contract_text(text)
    return {"filename": file.filename, "result": result}
