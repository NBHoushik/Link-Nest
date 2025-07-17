from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User,Link
from django.contrib.auth import authenticate, login
# used for qr code
import qrcode
from io import BytesIO
# Create your views here.
def home(request):
  return render(request,"Links/index.html")

def index(request):
  return render(request,"Links/index.html")

def signup(request):
  return render(request,"Links/signup.html")


#login check and checking existing of user 
def profile_check(request):
  if request.method=="POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    if User.objects.filter(username=username,password=password).exists() or User.objects.filter(email=username,password=password):
        try:
          user=get_object_or_404(User,username=username)
          username=user.username
        except:
          user=get_object_or_404(User,email=username)
          username=user.username
        return redirect('profile_page', username)
    else:   
      messages.error(request,"username or password is wrong")
      return redirect('index')
  return redirect('index')
#adding new user to database and checking for if user laredy exists 
def register_user(request):
  if request.method=="POST":
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    if username=="" or password=="":
      messages.error(request,"Enter valid data")
      return redirect('signup')
    if User.objects.filter(username=username).exists():
      messages.error(request,"Username already Exists")
      return redirect('signup')
    else:
      User.objects.create(username=username,email=email,password=password)
      return redirect('index')
  return redirect('index')
  


#showing links along with user name
def profile_page(request,username):
  user=get_object_or_404(User,username=username)
  user_links=Link.objects.filter(user=user)
  return render(request,"Links/profile.html",{"user_links":user_links,"username":username})

#adding new links page
def add_link_page(request,username):
  return render(request,"Links/add_link_page.html",{"username":username})

#adding new links to user
def add_link(request,username):
  user=User.objects.get(username=username)
  if request.method=="POST":
    linkname=request.POST.get("linkname")
    link=request.POST.get("link")
    description=request.POST.get("description")
    if Link.objects.filter(link=link).exists():
      messages.error(request,"Link alredy exists in profile")
      return redirect('add_link_page',username)
    else:
      Link.objects.create(user=user,name=linkname,link=link,description=description)
      messages.success(request,"Link added successfully")
  return redirect('add_link_page',username)

#delete or update the exixting links
def delete_update(request,link_id):
  link=get_object_or_404(Link,id=link_id)
  username=link.user.username 
  if request.method=="POST":
    action=request.POST.get("action")
    if action=="delete":  
      username=link.user.username
      link.delete()
      return redirect('profile_page',username)
    else:
      return render(request,"Links/update.html",{"link":link,"username":username})
    
#update the existing data      
def update(request,link_id):
  link=get_object_or_404(Link,id=link_id)
  if request.method=="POST":
    link.name=request.POST.get("name")
    link.link=request.POST.get("link")
    link.description=request.POST.get("description")
    link.save()
  username=link.user.username
  return redirect('profile_page',username)

#creating superlink for user
def link_nest(request,username):
  user=get_object_or_404(User,username=username)
  user_links=Link.objects.filter(user=user)
  return render(request,"Links/public_page.html",{"links":user_links,"username":username})

#generating QR code for the super link
def qr_code(request,username):
  url = f"http://127.0.0.1:8000/u/{username}/" 
  img=qrcode.make(url)
  buffer = BytesIO()
  img.save(buffer,format="PNG")
  return HttpResponse(buffer.getvalue(),content_type='image/png')