from django.contrib import admin
from .models import User,Pollsters,User_Pollsters
# Register your models here.
admin.site.register(User)
admin.site.register(Pollsters)
admin.site.register(User_Pollsters)