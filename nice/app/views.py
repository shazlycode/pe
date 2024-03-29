from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import DrugIndex
from .forms import Register, Login, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    context ={
        'title': 'Home',
    }
    return render(request, 'app/index.html', context)


def about(request):
    context={
        'title':'about',
        
    }
    return render(request, 'app/about.html', context)

def drugindex(request):
    trade_results=None
    generic_results=None
    uses_results=None
    
    drugs= DrugIndex.objects.all()
    trade_name_box=request.GET.get('trade_name_box')
    generic_name_box=request.GET.get('generic_name_box')
    uses_box=request.GET.get('uses_box')
    if trade_name_box !='' and trade_name_box is not None:
        trade_results= drugs.filter(trade_name__icontains=trade_name_box)
    elif generic_name_box !='' and generic_name_box is not None:
        generic_results= drugs.filter(generic_name__icontains=generic_name_box)
    elif uses_box !='' and uses_box is not None:
        uses_results=drugs.filter(uses__icontains=uses_box)
    
    
    
    
    context={
        'title':'Drug Index',
        'trade_results': trade_results,
        'generic_results': generic_results,
        'uses_results': uses_results,
        
        
    }
    return render(request, 'app/drugindex.html', context)


def register(request):
    register_form= Register()
    if request.method=='POST':
        register_form= Register(request.POST)
        if register_form.is_valid():
            new=register_form.save(commit=False)
            username= register_form.cleaned_data['username']
            password= register_form.cleaned_data['password1']
            new.set_password(password)
            new.save()
            messages.success(request,'Congratulations {} you have successfully registered'.format(username))
            return redirect('/login')
        
        
        
        
    else:
        register_form= Register()
    
    context={
        'title':'Register',
        'register':register_form,
    }
    
    return render(request, 'app/register.html', context)


def login_view(request):
    
    login_form=Login()
    if request.method=='POST':
        login_form=Login(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'{} you have successfully logged in'.format(username))
            return redirect('index')
        else:
            messages.warning(request,'username and/or password is incorrect')

    else:
        login_form=Login()
            
    context={
        'title':'Login',
        'login_form': login_form,
        
    }
    
    return render(request, 'app/login.html', context)

def logout_view(request):
    
    logout(request)
    context={
        'title':'Logout',
    }
    return render(request, 'app/logout.html', context)

def contactus(request):
    post_form= PostForm()
    if request.method=='POST':
        post_form= PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request,'Your message was sent. Thanks for feedback')
            return redirect('/contactus')
        
    else:
        post_form=PostForm()
    context={
        'title':'Contact us',
        'post_form': post_form,
    }
    
    return render(request, 'app/contactus.html', context)

def recent(request):
    context={
        'title':'Recent Updates',
    }
    return render(request, 'app/recent.html', context)

def interactions(request):
    context={
        'title':'Interactions',
    }
    return render(request, 'app/interactions.html', context)

def quize(request):
    context={
        'title':'Quize',
    }
    return render(request, 'app/quize.html', context)


def drug_details(request, drug_id):
    results=get_object_or_404(DrugIndex, pk=drug_id)
    
    
    
    context={
        'title':'Drug Details',
        'results':results,
    }
    
    return render(request, 'app/drug_details.html', context)