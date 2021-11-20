from django.contrib import admin
from django.urls import path ,include
from stonewall import views

urlpatterns = [
   path("", views.home, name='home'),
   path('admin/', admin.site.urls),
   path("mentalhealth", views.mentalhealth, name='mentalhealth'),
   path("findnearby", views.findnearby, name='findnearby'),
   path("organisations", views.organisations, name='organisations'),
   path("definitions", views.definitions, name='definitions'),
   path("pridesection", views.pridesection, name='pridesection'),
   path("blogshome", views.blogshome, name='blogshome'),
   path("contact", views.contact, name='contact'),
   path('froala_editor/',include('froala_editor.urls')),
   path("login/", views.login, name='login'),
   path("log_out/", views.log_out, name='log_out'),
   path("register/", views.register, name='register'),
   path("addblog/", views.addblog, name='addblog'),
   path("seeblog/", views.seeblog, name='seeblog'),
   path("blogdelete/<id>", views.blogdelete, name='blogdelete'),
   path("blogupdate/<slug>/", views.blogupdate, name='blogupdate'),
   path("verify/<token>/", views.verify, name='verify'),
   path('admin/', admin.site.urls),
   path('blogdetail/<slug>',views.blogdetail, name='blogdetail'),
   path('api/', include('stonewall.apiurls')),
    
   
]