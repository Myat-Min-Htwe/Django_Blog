from django.shortcuts import render,redirect

from .models import PostModel
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

@permission_required('my_blog.add_postmodel',login_url='login')
def post_create(request):
    
    if request.method == "GET":
        return render(request,'postCreate.html')
    
    if request.method == "POST":
        posts = PostModel.objects.create(
            title = request.POST.get('title'),
            body = request.POST.get('body'),
            created_at = request.POST.get('created')
        )
        posts.save()
        messages.success(request, "The post has been created successfully.")
        return redirect('/blog/')

@permission_required('my_blog.view_postmodel',login_url='login')
def post_list(request):
    posts = PostModel.objects.all().order_by('-created_at')
    return render(request,'postList.html',{'posts':posts})

@permission_required('my_blog.view_postmodel',login_url='login')
def post_detail(request,post_id):
     posts = PostModel.objects.get(id=post_id)
     return render(request,'postDetail.html',{'posts':posts})

@permission_required('my_blog.change_postmodel',login_url='login')
def post_update(request,post_id):
    if request.method == "GET":
        posts = PostModel.objects.get(id=post_id)
        posts.created_at = posts.created_at.strftime('%Y-%m-%dT%H:%M')
        return render(request,'postUpdate.html',{'posts':posts})
    
    if request.method == "POST":
        posts = PostModel.objects.get(id=post_id)

        posts.title = request.POST.get('title')
        posts.body = request.POST.get('body')
        posts.created_at = request.POST.get('created')
        posts.save()
        messages.success(request, "The post has been updated successfully.")
        return redirect('/blog/')
    
@permission_required('my_blog.delete_postmodel',login_url='login')
def post_delete(request,post_id):
    posts = PostModel.objects.filter(id=post_id)
    posts.delete()
    messages.success(request, "The post has been deleted successfully.")
    return redirect('/blog/')


def login_view(request):
    if request.method == "GET":
        return render(request,'login.html')
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in as " + username)
            return redirect('/blog/')
        else:
            messages.error(request, "Username or Password is incorrect !")
            return render(request, 'login.html')
        

def logout_view(request):
    logout(request)
    return redirect('/blog/login/')