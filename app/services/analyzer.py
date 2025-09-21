from app.config.settings import settings
import httpx

async def llm_complete(system: str, user: str) -> str:
    headers = {"Authorization": f"Bearer {settings.llm_api_key}"}
    base = settings.llm_base_url or "https://api.openai.com/v1"
    payload = {
        "model": settings.model_name,
        "messages": [
            {"role":"system","content":system},
            {"role":"user","content":user}
        ],
        "temperature": 0.2,
    }
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(f"{base}/chat/completions", json=payload, headers=headers)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"].strip()

async def analyze_contract_text(text: str) -> dict:
    from app.prompts import SUMMARY_PROMPT, CLAUSES_PROMPT, RISK_PROMPT
    system = "You are a precise legal assistant. Be concise and structured."
    summary = await llm_complete(system, f"{SUMMARY_PROMPT}\n\n---\n{text[:15000]}")
    clauses = await llm_complete(system, f"{CLAUSES_PROMPT}\n\n---\n{text[:15000]}")
    risks   = await llm_complete(system, f"{RISK_PROMPT}\n\n---\n{text[:15000]}")
    return {"summary": summary, "clauses": clauses, "risks": risks}
