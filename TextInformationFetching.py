from google import genai

client = genai.Client(api_key='GEMINI_API_KEY')
question = input("Enter your prompt here: ")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=question
)

with open("response.md", "w") as file:
    file.write(response.text)
print("Your response is ready in a file named \"response.md\"")