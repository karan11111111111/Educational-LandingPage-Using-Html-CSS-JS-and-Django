from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    context = {  # context: set of variables
        "variable1":"This is sent",
        "variable2":"This is sent 2"
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html',)
    # return HttpResponse("this is about page")

def courses(request):
    return render(request, 'courses.html',)
    # return HttpResponse("this is services page")

def contact(request):
    # return HttpResponse("this is Contact page")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
     

    return render(request, 'contact.html',)


