from django.contrib import admin
from .models import AbstractUser,FileModel,PermissionModel

# Register your models here.

admin.site.register(AbstractUser)
admin.site.register(FileModel)
admin.site.register(PermissionModel)
