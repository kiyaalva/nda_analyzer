# app/prompts.py

SUMMARY_PROMPT = """You are a legal analyst. Summarize the NDA in 5 concise bullet points:
- Parties and purpose
- Term & termination
- Confidentiality scope
- Use restrictions
- Notable obligations
Return short bullets."""

CLAUSES_PROMPT = """Extract these clauses (verbatim or close paraphrase) if present:
- Term / Duration
- Governing Law / Jurisdiction
- Indemnification
- Non-Disclosure Scope
Provide each as: Name: "Text"."""

RISK_PROMPT = """Flag unusual or risky items vs a typical mutual NDA.
Examples: indefinite confidentiality, broad IP assignment, unilateral jurisdiction, no survival clause, unlimited liability, ambiguous definitions.
Return a list of risks with one-line rationale."""
