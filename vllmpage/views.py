from django.shortcuts import render
from google.genai import types
from google import genai
import json

def home(request):
    return render(request, "vllmpage/home.html")



with open("C:/Users/assaf/Desktop/GDG_HACK/vllmpage/static/vllmpage/images/dummy.png", 'rb') as f:
    image_bytes = f.read()

client = genai.Client(api_key="AIzaSyAjPSVPSC9cPrKpsraxSkJvtdsn7WY5UpE")
response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
        ),
        """Give ONE random object from this image alongside it's coordinate of the center of the box in a json format. 
        The coordinates should be given as ratios of the image's dimensions.
        Use this JSON schema:

        {'object_name': str, 'x': float, 'y': float}"""
    ],
    
)

indices = []
for idx, char in enumerate(response.text):
    if char == "{" or char == "}":
        indices.append(idx)

objval = response.text[indices[0]: indices[1]+1]
objvalj = json.loads(objval)

def game(request):
    context={
        "obj_name": objvalj['object_name'],
        "image": "{% static 'vllmpage/images/dummy.jpg' %}",
        "x":objvalj['x'],
        "y":objvalj['y'],
    }

    return render(request, "vllmpage/game.html", context)