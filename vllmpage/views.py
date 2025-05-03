from django.shortcuts import render
from google.genai import types
from google import genai
import json
import random as rand
import os
from django.templatetags.static import static

def home(request):
    return render(request, "vllmpage/home.html")




def game(request):
    

    
    img_name = rand.choice(os.listdir("./vllmpage/static/vllmpage/images"))
    img_type = img_name.split(".", 1)[1]
    print(img_type, img_name)


    with open(f"./vllmpage/static/vllmpage/images/{img_name}", 'rb') as f:
        image_bytes = f.read()

    client = genai.Client(api_key="AIzaSyAjPSVPSC9cPrKpsraxSkJvtdsn7WY5UpE")
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=[
            types.Part.from_bytes(
            data=image_bytes,
            mime_type=f'image/{img_type}',
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
    print(objvalj['x'], objvalj['y'], objvalj['object_name'])




    context={
        "obj_name": objvalj['object_name'],
        "image_path": f"vllmpage/images/{img_name}",
        "xcoord":objvalj['x'],
        "ycoord":objvalj['y'],
    }
    return render(request, "vllmpage/game.html", context)