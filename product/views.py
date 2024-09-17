from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def indexpage(request):
    data= {"user1":[
           {"name":"shanmu","loc":"madu","score":90},
           {"name":"priyaa","loc":"chennai","score":94},
           {"name":"aruna","loc":"cbe","score":71},
           {"name":"harini","loc":"trichy","score":60}
           ]
    }
    return render(request,'home.html',data)
def aboutpage(request):
    return render(request,'about.html')
#_____________________________________________________________________

def productlist(request):
    data={"prolist":Product.objects.all()}
    print(data)
    return render(request,'productlist.html',data)
#___________________________________________________________________________
def productadd(request):
    data = {"proForm":ProductForm()}
    new_data = ProductForm (request.POST)
    if new_data.is_valid():
        new_data.save()
        return redirect ('/product/productlist/')
    return render(request,'productadd.html',data)
#_________________________________________________________________________________
def productdelete(request,id):
    selected_data = Product.objects.get(id=id)
    selected_data.delete()
    return  redirect ('/product/productlist/')

#_________________________________________________________________________________
def productupdate(request,id):
     selected_data = Product.objects.get(id=id)
     data = {"proForm":ProductForm(instance=selected_data)}

     if request.method == "POST":
         new_data=ProductForm(request.POST,instance=selected_data)
         if new_data.is_valid():
             new_data.save()
             return redirect('/product/productlist/')

     return render(request,'productadd.html',data)
#__________________________________________________________________________________

