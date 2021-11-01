from django.contrib import admin
from django.urls import path ,include
from stonewall import views

urlpatterns = [
   path("", views.home, name='home'),
   path('admin/', admin.site.urls),
   path("mentalhealth", views.mentalhealth, name='mentalhealth'),
   path("findnearby", views.findnearby, name='findnearby'),
   path("miniblogs", views.miniblogs, name='miniblogs'),
   path("organisations", views.organisations, name='organisations'),
   path("definitions", views.definitions, name='definitions'),
   path("pridesection", views.pridesection, name='pridesection'),
   path("contact", views.contact, name='contact'),
   path('froala_editor/',include('froala_editor.urls')),
   path('admin/', admin.site.urls),
   
]