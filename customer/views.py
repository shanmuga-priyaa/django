from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request,'index.html')
def header(request):
    return render(request,'about.html')
#___________________________________________________________________
def customerlist(request):
    data={"customerlist":customer.objects.all()}
    print(data)
    return render(request,'customerlist.html',data)
#___________________________________________________________________
def customeradd(request):
    data = {"custForm":customerForm()}
    new_data = customerForm (request.POST)
    if new_data.is_valid():
        new_data.save()
        return redirect ('/customer/customerlist/')
    return render(request,'customeradd.html',data)
#_________________________________________________________________________________
def customerdelete(request,id):
    selected_data = customer.objects.get(id=id)
    selected_data.delete()
    return  redirect ('/customer/customerlist/')

#_________________________________________________________________________________
def customerupdate(request,id):
     selected_data = customer.objects.get(id=id)
     data = {"custForm":customerForm(instance=selected_data)}

     if request.method == "POST":
         new_data=customerForm(request.POST,instance=selected_data)
         if new_data.is_valid():
             new_data.save()
             return redirect('/customer/customerlist/')

     return render(request,'customeradd.html',data)
#__________________________________________________________________________________
