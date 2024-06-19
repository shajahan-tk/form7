from django.shortcuts import render,redirect,get_object_or_404
from.models import*
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required 


# Create your views here.
def home(request):
    return render(request,'index.html')

@login_required
def form8(request):
    if request.method == 'POST':
        username = request.POST['username']
        clinicid = request.POST['clinicid']
        domainname = request.POST['domainname']
        
        # Check if username is not empty
        if main.objects.filter(clinicid=clinicid).exists():
            messages.error(request, 'Domine name or Username already exists.')
        elif main.objects.filter(username=username).exists():
            messages.error(request, 'Domine name or Username already exists.')
        else:
            myuser = main(username=username, clinicid=clinicid, domainname=domainname)
            myuser.save()
            messages.success(request, 'Data saved successfully.')
        return redirect('/form')
    
    xyz = main.objects.all()
    username_filter = request.GET.get('username_filter')
    if username_filter:
        xyz = xyz.filter(username=username_filter)
    paginator = Paginator(xyz, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'show': page_obj, 'username_filter': username_filter})
    
def delete(request,id):
    abc=main.objects.get(id=id)
    abc.delete()
    return redirect("/form")

def edit(request,id):
    abc=main.objects.get(id=id)
    abc.edit()
    return redirect("/form")

def edit(request,id):
    edit1=get_object_or_404(main,id=id)
    if request.method == 'POST':
        username=request.POST['username']
        clinicid=request.POST['clinicid']
        domainname=request.POST['domainname']
        edit1.username=username
        edit1.clinicid=clinicid
        domainname=domainname
        edit1.save()
        return redirect('/home')
    return render(request,'index.html',{'edit1':edit1})




















































































   
    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # User is authenticated, log them in
            logins(request, user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('/form')  # Redirect to the home page after successful login
        else:
            # Authentication failed, handle the error
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Redirect back to the login page with an error message
    else:
        # Handle GET request (e.g., render the login form)
        return render(request, 'login.html')  # Assuming you have a template named 'login.html'


def handlelogout(request):
    logout(request)
    return redirect('/login') 
      
     



