from django.shortcuts import render

def home(request):
    return render(request, "vllmpage/home.html")

def game(request):
    context={
        "obj_name": "test",
        "image": "{% static 'vllmpage/images/dummy.jpg' %}",
    }

    return render(request, "vllmpage/game.html", context)