import streamlit as st
from PIL import Image
import pytesseract
from transformers import pipeline
import os
import openai  # Only if you're using GPT for detailed explanations

# 🧠 OPTIONAL: If you want GPT to give deeper insights
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace this if needed

# 🔧 Configure pytesseract path (change if yours is different)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 💻 Streamlit UI
st.set_page_config(page_title="Medical Report Analyzer", layout="wide")
st.title("🧾 Medical Report Analyzer & Explainer")
st.write("Upload a scanned medical report to extract and explain its content in simple terms.")

uploaded_file = st.file_uploader("Upload a medical report image (PNG or JPG)", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Report', use_container_width=True)

    with st.spinner("🔍 Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)
        st.subheader("📄 Extracted Text")
        st.text_area("Text from image:", extracted_text, height=300)

    with st.spinner("🧠 Summarizing medical content..."):
        summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base")
        summary = summarizer(extracted_text, max_length=180, min_length=30, do_sample=False)[0]['summary_text']
        st.subheader("📝 Summary")
        st.success(summary)

    with st.spinner("💬 Generating patient-friendly explanation..."):
        prompt = f"""You are a medical assistant. Explain the following summary of a medical report to a non-medical person. 
        Include what the condition is, possible causes, common symptoms, and what it might mean in simple terms. 
        Here's the summary: {summary}"""

        # Call OpenAI or any LLM (this example uses OpenAI)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        explanation = response["choices"][0]["message"]["content"]

        st.subheader("🩺 Easy-to-Understand Explanation")
        st.info(explanation)
