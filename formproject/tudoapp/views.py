from django.shortcuts import render,redirect,get_object_or_404
from.models import*
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'index.html')

def form8(request):
    if request.method == 'POST':
        username = request.POST['username']
        domainname = request.POST['domainname']
        myuser = main(username=username, domainname=domainname)
        myuser.save()
        messages.success(request, 'Data saved successfully.')
        return redirect('/form')
    
    xyz = main.objects.all()
    return render(request, 'index.html', {'show': xyz, })
    
def delete(request,id):
    abc=main.objects.get(id=id)
    abc.delete()
    return redirect("/form")




def edit(request,id):
    edit1=get_object_or_404(main,id=id)
    if request.method == 'POST':
        username=request.POST['username']
        domainname=request.POST['domainname']
        edit1.username=username
        domainname=domainname
        edit1.save()
        return redirect('/home')
    return render(request,'index.html',{'edit1':edit1})




















































































   

      
     



