
from django.shortcuts import render
from .models import mahajan
from .forms import aman
from confirm import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    fm=aman()
    if request.method=="POST":
        n1=request.POST['name']
        n2=request.POST['roll_no']
        n3=request.POST['college_name']
        n4=request.POST['degree']
        n5=request.POST['branch']
        n6=request.POST['section_name']
        n7=request.POST['select_course']
        n8=request.POST['email']
        user=mahajan(name=n1,roll_no=n2,college_name=n3,degree=n4,branch=n5,section_name=n6,select_course=n7,email=n8)
        user.save()
        #email
        subject="Welcome to mahajan course wallah"
        message="hello"+user.name+"i am mahajn coding wallah i want to welcome to in our service"
        from_email=settings.EMAIL_HOST_USER
        to_email=[user.email]
        send_mail(subject,message,from_email,to_email,fail_silently=True)


    
    return render(request,"home.html",{'forms':fm})