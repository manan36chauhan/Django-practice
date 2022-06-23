from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("This is about us")
def services(request):
    return HttpResponse("I am your services")