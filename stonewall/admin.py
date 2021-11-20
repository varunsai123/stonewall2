from django.contrib import admin
from stonewall.models import Contact, Profile
from stonewall.models import BlogModel
# Register your models here.
admin.site.register(Contact)
admin.site.register(BlogModel)
admin.site.register(Profile)
