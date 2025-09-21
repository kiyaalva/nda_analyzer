import streamlit as st, requests, os
API_URL = os.getenv("API_URL","http://127.0.0.1:8000/analyze")

st.title("NDA Analyzer (MVP)")
file = st.file_uploader("Upload NDA (PDF or DOCX)", type=["pdf","docx"])

if st.button("Analyze") and file:
    with st.spinner("Analyzing..."):
        files = {"file": (file.name, file.getvalue(), file.type)}
        r = requests.post(API_URL, files=files, timeout=120)
        if r.ok:
            data = r.json()["result"]
            st.subheader("Summary");      st.write(data["summary"])
            st.subheader("Key Clauses");  st.write(data["clauses"])
            st.subheader("Risk Flags");   st.write(data["risks"])
        else:
            st.error(f"Error: {r.status_code} - {r.text}")
