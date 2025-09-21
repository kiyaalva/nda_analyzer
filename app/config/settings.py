from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseModel):
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_base_url: str | None = os.getenv("LLM_BASE_URL") or None
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    store_documents: bool = (os.getenv("STORE_DOCUMENTS","false").lower()=="true")

settings = Settings()
