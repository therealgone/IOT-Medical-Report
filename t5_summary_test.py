import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from PIL import Image
import pytesseract

# 📥 Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 🔑 Set up Gemini with the latest pro model
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")

# 🔧 Tesseract path (Update if different on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🖥️ Streamlit UI Setup
st.set_page_config(page_title="Medical Report Analyzer", layout="wide")
st.title("🧾 Medical Report Analyzer & Patient-Friendly Explainer")
st.markdown("Upload a **scanned medical report**, and I’ll extract, summarize, and explain it in simple terms for better understanding.")

# 📤 Upload Section
uploaded_file = st.file_uploader("📎 Upload a report image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="📄 Uploaded Medical Report", use_container_width=True)

    with st.spinner("🔍 Extracting text using OCR..."):
        extracted_text = pytesseract.image_to_string(image)
        st.subheader("📝 Extracted Raw Text")
        st.text_area("OCR Output", extracted_text, height=250)

    if extracted_text.strip():
        with st.spinner("🧠 Analyzing and explaining the report using Gemini..."):
            prompt = f"""
You are a kind and smart medical assistant who helps people understand medical reports.

Here's the extracted text from a scanned medical report:

\"\"\"{extracted_text}\"\"\"

Do the following:
1. 🔍 Summarize the report in 5 simple lines.
2. 🧠 Identify the possible medical conditions (if any) mentioned.
3. 📋 Explain the conditions in simple, easy-to-understand words.
4. 😷 List common symptoms and causes.
5. 💊 Suggest what the patient should do next (e.g., tests, treatment, lifestyle).
6. 🇮🇳 Use a tone that an Indian college student or family can understand clearly.

Make sure the answer is:
- Easy to read
- Non-technical
- Supportive and positive in tone
            """

            response = model.generate_content([prompt, image])
            explanation = response.text

            st.subheader("🩺 Easy-to-Understand Report Summary")
            st.info(explanation)
    else:
        st.warning("⚠️ No readable text found in the image.")
