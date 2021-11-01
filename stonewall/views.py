
from django.shortcuts import render, HttpResponse
from datetime import datetime
from stonewall.models import Contact
# Create your views here.
def home(request):
    return render(request, 'home.html')    
def mentalhealth(request):
    return render(request, 'mentalhealth.html')
def findnearby(request):
    return render(request, 'findnearby.html')
def miniblogs(request):
    return render(request, 'miniblogs.html')
def organisations(request):
    return render(request, 'organisations.html')
def definitions(request):
    return render(request, 'definitions.html')
def pridesection(request):
    return render(request, 'pridesection.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email=email , desc=desc, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')    