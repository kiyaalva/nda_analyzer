import docx2txt, tempfile, os
def extract_text_from_docx(file_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name
    try:
        return docx2txt.process(tmp_path) or ""
    finally:
        os.remove(tmp_path)
