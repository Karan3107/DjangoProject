from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from Sharing.models import AbstractUser
from .forms import UploadFileForm
from .permissionform import PermissionForm
from .models import FileModel,PermissionModel

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        Alluser = User.objects.all()
        print(Alluser)
        form = UploadFileForm()
        Allfiles = FileModel.objects.filter(owner = request.user)
        return render(request, 'index.html',{'form':form, 'user':request.user, 'Allfiles':Allfiles, 'Alluser':Alluser})
    else:
        return redirect('login')

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        abuser = AbstractUser(username=username, email=email, phone=phone, mainuser = user)
        abuser.save()
        return redirect('/')
    return render(request,'register.html')

def uploadFile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
    return redirect('dashboard')

def deleteFile(request,pk):
    if request.method == 'POST':
        file = FileModel.objects.get(pk=pk)
        print(file)
        file.delete()
    return redirect('dashboard')

def shareFile(request,pk):
    if request.method == 'POST':
        file = FileModel.objects.get(pk=pk)
        print(file)
        Allemail = request.POST.getlist('Allselected')
        print(Allemail)
        for email in Allemail:
            user = User.objects.get(email=email)
            if user is not None:
                permission = PermissionModel(document=file, ruser=user, suser = request.user.email)
                permission.save()
        return redirect('dashboard')
    else:
        Alluser = User.objects.all()
        return render(request, 'share.html',{'Alluser': Alluser,'pk':pk})

def recievedFile(request):
    if request.user.is_authenticated:
        Allpermission = PermissionModel.objects.filter(ruser = request.user)
        Allfiles = []
        suser = []
        for permission in Allpermission:
            Allfiles.append(permission.document)
        return render(request,'recieved.html',{'Allfiles':Allfiles, 'user':request.user})
    else:
        return redirect('/')

def deletePermission(request,pk):
    if request.method == 'POST':
        file = PermissionModel.objects.get(pk=pk)
        file.delete()
    return redirect('dashboard')