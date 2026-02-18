import google.generativeai as genai

API_KEY = "AIzaSyBfgKFnz-dzhOFIsyRJO81znTkVG-m3gl8"
genai.configure(api_key=API_KEY)

print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"- {model.name}")
