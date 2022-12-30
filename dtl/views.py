from django.shortcuts import render, HttpResponse

def home(request):
   # num=40
    #content = {}
    #content['data']=num
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')

# def dashboard(request):
    if request.method=="POST":
        return HttpResponse("IN POST")
    else:
        return render(request,'dashboard.html')