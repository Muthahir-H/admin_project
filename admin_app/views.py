
from django.shortcuts import render,redirect
from .forms import AuthorForm,BookForm

from .models import Book,Author
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages,auth





def createbook(request):

    books=Book.objects.all()

    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=BookForm()

    return render(request,'admin/book.html',{'form':form,'books':books})


def createauthor(request):


    if request.method=='POST':
        form=AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('createbook')

    else:
        form=AuthorForm()

    return render(request,'admin/author.html',{'form':form})


def listBook(request):

    books=Book.objects.all()
    paginator=Paginator(books,4)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)


    return render(request,'admin/listbook.html',{'books':books,'page':page})


def detailView(request):
    book=Book.objects.all()
    return render(request,'admin/detailview.html',{'book':book})


def updateBook(request,book_id):
    book = Book.objects.get(id=book_id)

    if request.method=='POST':
        form=BookForm(request.POST,files=request.FILES,instance=book)

        if form.is_valid:
            form.save()
            return redirect('/')
        
    else:
        form=BookForm(instance=book)

    return render(request,'admin/updateview.html',{'form':form})



def deleteView(request,book_id):
    book=Book.objects.get(id=book_id)

    if request.method=="POST":
        
        book.delete()

        return redirect('/')
    
    return render(request,'admin/deleteview.html',{'book':book})


def Index(request):
    return render(request,'admin/index.html')


def Search_Book(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)


def Register_User(request):
    if request.method=='POST':

        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This useraname already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This mail id already taken')
                return redirect('register')
            
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
            return redirect('login')
        else:
            messages.info(request,'This password not matching')
            return redirect('register')

    return render(request,'register.html')


def LoginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('createbook')
        else:
            messages.info(request,'Please Provide Correct Details')
            return redirect('login')
        
    return render(request,'login.html')


def Logout(request):
    auth.logout(request)
    return redirect('login')

