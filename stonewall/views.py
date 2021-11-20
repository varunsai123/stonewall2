
from typing import ContextManager
from django.shortcuts import render, redirect
from datetime import datetime
from stonewall.models import *
from .form import BlogForm
from django.contrib.auth import logout

# Create your views here.
def log_out(request):
    logout(request)
    return redirect('bloghome')

def home(request):
    return render(request, 'home.html')    
def mentalhealth(request):
    return render(request, 'mentalhealth.html')
def findnearby(request):
    return render(request, 'findnearby.html')
def organisations(request):
    return render(request, 'organisations.html')
def definitions(request):
    return render(request, 'definitions.html')
def pridesection(request):
    return render(request, 'pridesection.html')
def blogshome(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'blogshome.html', context) 
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def blogdetail(request,slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug = slug).first()
        context['blog_obj'] =  blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blogdetail.html', context)      
def addblog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            print(blog_obj)
            return redirect('/addblog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'addblog.html' , context)
                  
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name= name, email=email , desc=desc, date= datetime.today())
        contact.save()
    return render(request, 'contact.html')    

def seeblog(request):
    context = {}
    
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] =  blog_objs
    except Exception as e: 
        print(e)
    
    print(context)
    return render(request , 'seeblog.html' ,context)

def blogupdate(request , slug):
    context = {}
    try:
        
        
        blog_obj = BlogModel.objects.get(slug = slug)
       
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial = initial_dict)
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
        
        
        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e :
        print(e)

    return render(request , 'updateblog.html' , context)

def blogdelete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()
        
    except Exception as e :
        print(e)

    return redirect('/seeblog/')

def verify(request,token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()
        
        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        return redirect('/login/')

    except Exception as e : 
        print(e)
    
    return redirect('/')    

