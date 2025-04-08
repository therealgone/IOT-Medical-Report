# IOT-Medical-Report 🏥


## Overview 🌟
**IOT-Medical-Report** is an innovative solution designed to assist in the processing and understanding of medical reports. By using advanced machine learning and AI models, this project extracts text from uploaded medical documents (like scanned reports) and generates easy-to-understand explanations for users. It helps insurance professionals, medical practitioners, and families to interpret complex medical data and decide on the legitimacy of claims.

Currently, the project processes **scanned medical reports** and provides a summary of the extracted text. The support for **X-ray** and **MRI scan** processing is still under development.

---

## Features ✨
- **OCR (Optical Character Recognition)**: Extracts text from scanned medical reports (PDFs, PNG, JPG, JPEG).
- **Medical Report Summarization**: Automatically summarizes the extracted text in simple terms.
- **Medical Condition Identification**: Identifies possible medical conditions mentioned in the report.
- **Simplified Explanations**: Provides an easy-to-understand explanation of medical conditions for users, especially those without a technical background.
- **Support for Insurance Claims**: Helps insurance professionals verify if medical claims are legitimate based on the content of the reports.

### Future Features (Under Development) 🚀
- **X-ray & MRI Scan Analysis**: Integration of machine learning models to analyze X-ray and MRI scans alongside medical records for better insights.

---

## Requirements 📋

To run this project, you'll need to install the required dependencies. Here's the `requirements.txt`:

```plaintext
altair==5.5.0
annotated-types==0.7.0
anyio==4.9.0
attrs==25.3.0
blinker==1.9.0
cachetools==5.5.2
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
distro==1.9.0
filelock==3.18.0
fsspec==2025.3.2
gitdb==4.0.12
GitPython==3.1.44
google-ai-generativelanguage==0.6.15
google-api-core==2.24.2
google-api-python-client==2.166.0
google-auth==2.38.0
google-auth-httplib2==0.2.0
google-generativeai==0.8.4
googleapis-common-protos==1.69.2
grpcio==1.71.0
grpcio-status==1.71.0
h11==0.14.0
httpcore==1.0.7
httplib2==0.22.0
httpx==0.28.1
huggingface-hub==0.30.1
idna==3.10
Jinja2==3.1.6
jiter==0.9.0
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
MarkupSafe==3.0.2
mpmath==1.3.0
narwhals==1.34.0
networkx==3.4.2
numpy==2.2.4
openai==1.70.0
packaging==24.2
pandas==2.2.3
pillow==11.1.0
proto-plus==1.26.1
protobuf==5.29.4
pyarrow==19.0.1
pyasn1==0.6.1
pyasn1_modules==0.4.2
pydantic==2.11.2
pydantic_core==2.33.1
pydeck==0.9.1
pyparsing==3.2.3
pytesseract==0.3.13
python-dateutil==2.9.0.post0
python-dotenv==1.1.0
pytz==2025.2
PyYAML==6.0.2
referencing==0.36.2
regex==2024.11.6
requests==2.32.3
rpds-py==0.24.0
rsa==4.9
safetensors==0.5.3
sentencepiece==0.2.0
six==1.17.0
smmap==5.0.2
sniffio==1.3.1
streamlit==1.44.1
sympy==1.13.1
tenacity==9.1.2
tokenizers==0.15.2
toml==0.10.2
torch==2.6.0
tornado==6.4.2
tqdm==4.67.1
transformers==4.37.2
typing-inspection==0.4.0
typing_extensions==4.13.1
tzdata==2025.2
uritemplate==4.1.1
urllib3==2.3.0
watchdog==6.0.0

```
## Installation 🛠️

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/IOT-Medical-Report.git
```
### 2. Navigate into the project directory:
```bash
cd IOT-Medical-Report
```
### 3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
### 4. Set up environment variables:
```Create a .env file in the root of the project and add your Google API key.
GOOGLE_API_KEY=your_google_api_key_here
```
###5. Run the application:
```bash
streamlit run app.py
```


Usage 🖥️
Once the app is running, you can upload a scanned medical report (in formats like PNG, JPG, JPEG) using the file uploader in the Streamlit UI. The app will:

Extract the text from the medical report using OCR.

Provide an easy-to-understand summary of the report, highlighting key medical conditions.

Explain those conditions in simple, non-technical language.

Offer helpful suggestions for next steps based on the extracted content.

Project Status ⚡
Medical Report Summarization: ✅ Completed

X-ray/MRI Scan Analysis: ⏳ Under Development

Contributing 🤝
We welcome contributions! If you'd like to contribute, please fork the repository and create a pull request. Here are some ways you can contribute:

Fix bugs or improve the codebase.

Enhance the OCR or AI capabilities.

Improve documentation.

License 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Created by Jeevan.
For any queries or suggestions, feel free to open an issue or contact me via email.



