from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "context":"context bilgisidir",
        }
    return render(request,"index.html",context)
