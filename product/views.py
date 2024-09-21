from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View

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
 
class ProductListView(View):
    def get(self,request):
        data={"prolist":Product.objects.all()}
        print(data)
        return render(request,'productlist.html',data)
#___________________________________________________________________________

class ProductAddView(View):
    def get(self,request):
        data = {"proForm":ProductForm()}
        return render(request,'productadd.html',data)
    def post(self,request):
        new_data=ProductForm(request.POST,request.FILES)
        if new_data.is_valid():
            new_data.save()
            return redirect ('/product/productlist/')

#_________________________________________________________________________________

class ProductDeleteView(View):
    def get (self,request,id):
        selected_data = Product.objects.get(id=id)
        selected_data.delete()
        return  redirect ('/product/productlist/')
#_________________________________________________________________________________

class ProductUpdateView(View):
    def get(self,request,id):
        selected_data = Product.objects.get(id=id)
        data = {"proForm":ProductForm(instance=selected_data)}
        return render(request,'productadd.html',data)
    def post(self,request,id):
        selected_data = Product.objects.get(id=id)
        new_data=ProductForm(request.POST,instance=selected_data)
        if new_data.is_valid():
            new_data.save()
            return redirect('/product/productlist/')
#__________________________________________________________________________________

