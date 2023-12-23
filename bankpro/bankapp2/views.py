from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def register(request):
    if request == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user=User.objects.create_user(username=username,password=password)
        user.save();

    return render(request,'register.html')