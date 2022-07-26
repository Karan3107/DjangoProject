from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AbstractUser(models.Model):
    mainuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class FileModel(models.Model):
    name = models.CharField(max_length=255)
    fileurl = models.FileField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.fileurl.delete()
        super().delete(*args, **kwargs)
    


class PermissionModel(models.Model):
    document = models.ForeignKey(FileModel, on_delete=models.CASCADE, null=True)
    ruser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    suser = models.EmailField(max_length=255,null=True)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
