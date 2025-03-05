from google import genai 
from google.genai import types
from PIL import Image

image = Image.open('./path/to/file')

print("Reading Image....")
client = genai.Client(api_key='GEMINI-API-KEY')
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["What is this image?", image]
)

print("Printing Response...")
with open("response.md", "w") as file:
    file.write(response.text)

print("The response for this image is stored in response.md")