import fitz
print("PyMuPDF OK:", fitz.__doc__ is not None)

import os; from dotenv import load_dotenv; load_dotenv()
print("Key present:", bool(os.getenv("LLM_API_KEY")))