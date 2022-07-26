from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from Sharing import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.loginUser, name='login'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('logout',views.logoutUser, name='logout'),
    path('register',views.registerUser, name='register'),
    path('upload',views.uploadFile, name='upload'),
    path('delete/<int:pk>', views.deleteFile, name='delete'),
    path('share/<int:pk>', views.shareFile, name='share'),
    path('dashboard/recieved', views.recievedFile, name='recieved'),
    path('delete-permission/<int:pk>',views.deletePermission, name='deletePermission')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
