import streamlit as st
import requests

st.set_page_config(page_title="AI Document Compliance Checker", layout="wide")

st.title("🧠 AI Document Compliance Checker")
st.write("Upload a PDF or Word file to analyze, correct, and download for compliance, grammar, and sentiment scoring.")

# ---------------- Session State ----------------
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "file_uploaded" not in st.session_state:
    st.session_state.file_uploaded = None
if "output_format" not in st.session_state:
    st.session_state.output_format = "DOCX"
if "corrected_content" not in st.session_state:
    st.session_state.corrected_content = None

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader("📂 Upload File", type=["pdf", "docx"])
if uploaded_file:
    st.session_state.file_uploaded = uploaded_file
    st.success(f"✅ File Uploaded: {uploaded_file.name}")

# ---------------- Analyze Button ----------------
if st.session_state.file_uploaded and st.button("🔍 Analyze Document"):
    with st.spinner("Analyzing document... please wait..."):
        try:
            files = {
                "file": (
                    st.session_state.file_uploaded.name,
                    st.session_state.file_uploaded,
                    st.session_state.file_uploaded.type,
                )
            }
            response = requests.post("http://127.0.0.1:8000/analyze_file", files=files)
            if response.status_code == 200:
                st.session_state.analysis_result = response.json()
                st.session_state.corrected_content = None  # Reset corrected content
                st.success("✅ Document analyzed successfully!")
            else:
                st.error(f"❌ Backend error: {response.text}")
        except Exception as e:
            st.error(f"⚠️ Connection error: {e}")

# ---------------- Show Analysis ----------------
if st.session_state.analysis_result:
    result = st.session_state.analysis_result
    st.subheader("📄 Document Summary")
    st.write(result.get("summary", "No summary available."))

    col1, col2, col3 = st.columns(3)
    col1.metric("🧮 Grammar Score", f"{result.get('grammar_score', 'N/A')}/100")
    col2.metric("📊 Compliance", result.get("compliance_score", "N/A"))
    col3.metric("💬 Sentiment", result.get("sentiment", "Unknown"))

    st.markdown("---")
    st.subheader("🛠 Recommendations")
    recs = result.get("recommendations", [])
    if recs:
        for r in recs:
            st.write(f"✅ {r}")
    else:
        st.info("No recommendations available.")

# ---------------- Output Format Selection ----------------
if st.session_state.file_uploaded:
    st.markdown("### 🧾 Choose Output Format")
    st.session_state.output_format = st.radio(
        "Select download format:",
        ["DOCX", "PDF"],
        horizontal=True,
        key="format_choice",
    )

# ---------------- Correct & Download ----------------
if st.session_state.file_uploaded and st.button("✍️ Correct & Generate Document"):
    with st.spinner("Correcting and preparing your file..."):
        try:
            files = {
                "file": (
                    st.session_state.file_uploaded.name,
                    st.session_state.file_uploaded,
                    st.session_state.file_uploaded.type,
                )
            }
            response = requests.post("http://127.0.0.1:8000/correct_file", files=files)

            if response.status_code == 200:
                st.session_state.corrected_content = response.content
                st.success("✅ Document corrected successfully!")
            else:
                st.error(f"❌ Correction API Error: {response.text}")

        except Exception as e:
            st.error(f"⚠️ Connection error: {e}")

# ---------------- Persistent Download Button ----------------
if st.session_state.corrected_content:
    file_ext = "docx" if st.session_state.output_format == "DOCX" else "pdf"
    mime_type = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        if file_ext == "docx"
        else "application/pdf"
    )
    file_name = f"Corrected_{st.session_state.file_uploaded.name.split('.')[0]}.{file_ext}"

    st.download_button(
        label=f"⬇️ Download Corrected {file_ext.upper()} File",
        data=st.session_state.corrected_content,
        file_name=file_name,
        mime=mime_type,
    )
