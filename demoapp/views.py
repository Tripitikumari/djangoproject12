from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return render(request, "demoapp/home.html" )
def mul_view(request):
    if request.method=="POST":
        first= request.POST.get("first")
        second= request.POST.get("second")
        total= int(first) * int(second)
        return HttpResponse(f"<h1> mul of {first} and {second} no is{ total}</h1>")

    return render(request,"demoapp/mul.html")
 
