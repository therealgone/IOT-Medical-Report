import google.generativeai as genai

# Replace with your API key
genai.configure(api_key="ENTER THE API KEY")

models = genai.list_models()

for model in models:
    print(f"📌 Name: {model.name}")
    print(f"✅ Supported Methods: {model.supported_generation_methods}\n")
