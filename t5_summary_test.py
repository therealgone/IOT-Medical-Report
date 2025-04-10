import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
import tempfile

# 📥 Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 🔑 Set up Gemini with the latest pro model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# 🔧 Tesseract path (Update if different on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# 🖥️ Streamlit UI Setup
st.set_page_config(page_title="Medical Report Analyzer", layout="wide")
st.title("🧾 Medical Report Analyzer & Insurance Claim Checker")
st.markdown("Upload **multiple report images or a PDF**. I’ll extract, summarize, and analyze it for possible insurance claim eligibility.")

# 📤 Upload Section
uploaded_files = st.file_uploader("📎 Upload report images or a PDF", type=["png", "jpg", "jpeg", "pdf"], accept_multiple_files=True)

all_text = ""
images_for_preview = []

if uploaded_files:
    with st.spinner("📄 Processing uploaded files..."):
        for file in uploaded_files:
            if file.type == "application/pdf":
                images = convert_from_bytes(file.read())
                for img in images:
                    text = pytesseract.image_to_string(img)
                    all_text += text + "\n"
                    images_for_preview.append(img)
            else:
                img = Image.open(file)
                text = pytesseract.image_to_string(img)
                all_text += text + "\n"
                images_for_preview.append(img)

    st.subheader("🖼️ Preview of Uploaded Pages")
    st.image(images_for_preview, use_container_width=True)

    st.subheader("📝 Extracted OCR Text")
    st.text_area("Extracted Text", all_text.strip(), height=300)

    if all_text.strip():
        with st.spinner("🧠 Analyzing and summarizing the report using Gemini..."):
            prompt = f'''
You are a kind and smart medical assistant working for an Indian health insurance company.

The following text was extracted from a scanned medical report:
"""{all_text}"""

Your tasks:
1. 🔍 Summarize the medical report in 5 simple lines.
2. 🧠 Identify the mentioned medical condition(s).
3. 📋 Explain the condition(s) in very simple, clear language.
4. 😷 List possible symptoms and causes.
5. 💊 Suggest next steps for the patient (tests, treatment, rest, etc).
6. ✅ Analyze this report from an insurance perspective:
   - Identify the type of treatment (OPD, surgery, inpatient care, diagnostic, etc)
   - Is it related to any pre-existing condition?
   - Is there proof of hospital admission or treatment?
   - Under what claim category does this report fall?
7. 🇮🇳 Make your explanation suitable for Indian families and college students.
8. Check if there is any red flages if the symothes and the docter report are correct or any issue with the report
Answer in a helpful way like an insurance assistant would.
Be supportive, clear, and avoid medical jargon.
'''
            response = model.generate_content([prompt])
            st.subheader("📋 Gemini Summary & Insurance Report")
            st.info(response.text)
    else:
        st.warning("⚠️ No readable text found in the images or PDF.")
