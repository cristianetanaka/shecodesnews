from django.contrib import admin
from .import models
#from django.contrib.auth.models import Group, CustomUser
#from .models import CustomUser, UserProfile
#from .models import Profile


# unregister groups
#admin.site.unregister(Group)
    #model = Profile
# Extend User Model
#class UserAdmin(admin.ModelAdmin):
    #model = User
    #fields = [" "]
    #inlines = [ProfileInline]


# Register your models here.
admin.site.register(models.CustomUser)
