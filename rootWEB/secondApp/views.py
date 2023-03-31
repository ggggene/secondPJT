from django.shortcuts import render

# Create your views here.
def index(request) :
    print(">>>>>> DEBUG : 127.0.0.1:8000/second/index")
    return render(request,'second/index.html')