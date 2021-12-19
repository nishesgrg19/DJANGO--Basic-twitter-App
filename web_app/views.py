from django.shortcuts import redirect, render
from web_app.models import News
from web_app.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
@login_required
def index (request):
    news=News.objects.all()
    return render(request,'web_app/index.html',{'News':news})
    
@login_required
def add(request):
    if request.method=="GET":
        return render(request,'web_app/addnews.html')
    else:
        title=request.POST['title']
        content=request.POST['content']
        if content == "":
            messages.warning(request,'Plz  fill completly')
            return redirect('add')
        elif title=="":
            messages.warning(request,'Plz  fill completly')
            return redirect('add')
        else:
            News.objects.create(title=title,content=content,is_completed=True,author_id=request.user.id)
            return redirect('index')

    
def delete(request,id):
    news=News.objects.get(id=id)
    news.delete()
    return redirect('index')

def edit(request,id):
    news=News.objects.get(id=id)
    if request.method=="GET":
        return render(request,'web_app/edit.html',{'News':news})
    else:
        news.title=request.POST['title']
        news.content=request.POST['content']
        news.save()
        return redirect('index')
       

def sign_in(request):
    if request.method =="GET":
        return render(request,'User/sign-in.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        next_url=request.GET.get('next')
        if user is not None:
            login(request,user)
            messages.success(request,'successfully logged in....')
            if next_url is not None:
                return redirect(next_url)
            else:
               
                return redirect('index')
                
                
            
                
        else:
            messages.warning(request,'Please fill your logininfo')
            return redirect('sign-in')
        
def sign_out(request):
    logout(request)
    return redirect('sign-in')

def info(request):
    return render(request,'User/info.html')

def reset(request):
    if request.method=="GET":
        return render(request,'User/reset.html')
    else:
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        user=authenticate(request,username=request.user.username,password=oldpassword)
        if user is not None:
            user.set_password(newpassword)
            user.save()
            sign_out(request)
            return redirect('sign-in')
        else:
            return redirect('reset')
def register(request):
    if request.method=="GET":
        return render(request,'User/Register.html')
    else:
       username= request.POST['username']
       email= request.POST['email']
       password= request.POST['password']
       confirm_password=request.POST['confirm_password']
       if password==confirm_password:
         User.objects.create_user(username=username,email=email,password=password)
         send_message(username,email,type='register')
         return redirect('index')
       else:
           messages.error(request,'Your password doesnot match.')
           return redirect('register')
def contact(request):
    if request.method=="GET":
        return render(request,'User/contact.html')
    else:
        email=request.POST['email']
        descriptions= request.POST['content']
        send_message(email,descriptions,type='enquiry')
        return redirect('index')
        
def send_message(param1,param2,type):
    if type=="register":
        subject='Account has been created'
        content=f"Your account has been created and your username is {param1}"
        email=param2
    else:
        subject='Message received'
        content=param2
        email='nishesgrg18@gmail.com'
    send_mail(
        subject,
        content,
        'nishesgrg18@gmail.com',
        [email],
        fail_silently=False,
            )
        



        
    
    
    
    