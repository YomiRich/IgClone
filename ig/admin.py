from django.contrib import admin
from .models import Category,Location,Image,UserProfile
# Register your models here.

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)
admin.site.register(UserProfile)