from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,"home.html")

def select(request):
    userdata = checking.objects.all()
    print(userdata)
    insertdata = checkin() 
    if(request.method == "POST"):
        form = checkin(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/select')
    else:
        insertdata = checkin()
        return render(request,"select.html",{"formu":insertdata,"userdata":userdata})
    
 
def registerchecker(request):
    insert = writechecker()
    if(request.method == "POST"):
        form = writechecker(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/login')
    else:
        insert = writechecker()
        return render(request,"registerfchecker.html",{"myform":insert})




def delete(request,id):
    id=id
    x = checking.objects.get(id = id)
    print(x.first_name)
    form =checkout()
    print()
    if(request.method == 'POST'):
        form = checkout(request.POST)
        if(form.is_valid()):
            form.save()
            x.delete()
            return redirect('/select')
    else:
        form = checkout()  
    cont = {'done': x,'fini': form}  
    return render(request,'del.html',cont)
  
 
def update(request, id):
    info = checking.objects.get(id = id)
    if(request.method == 'POST'):
        form = checkin(request.POST,instance = info)
        if(form.is_valid()):
            info.save()
            return redirect('/select')
    else:
        form = checkin(instance = info)
    cont = {'done': form,'fini': info}
    return render(request,"update.html",cont)

    
def login(request):
    if(request.method == 'POST'):
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        userdata = checker.objects.filter(phone =phone,password = password)
        if(len(userdata)>0):
            return redirect('/select')
        else:
            return render(request,'login.html',{"notdata":"<b> you are not registed!</b>"})
        
    return render(request,'login.html',{"notdata":"<b> you are not registed!</b>"})
    
    


