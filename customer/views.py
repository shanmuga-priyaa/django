from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views import View

def home(request):
    return render(request,'index.html')
def header(request):
    return render(request,'about.html')
#___________________________________________________________________

class customerlistView(View):
    def get(self,request):
        data={"customerlist":customer.objects.all()}
        print(data)
        return render(request,'customerlist.html',data)

#___________________________________________________________________

class customeraddView(View):
    def get(self,request):
        data = {"custForm":customerForm()}
        return render(request,'customeradd.html',data)
    def post(self,request):
        new_data=customerForm(request.POST)
        if new_data.is_valid():
            new_data.save()
            return redirect ('/customer/customerlist/')
#_________________________________________________________________________________
class customerdeleteView(View):
    def get(self,request,id):
        selected_data = customer.objects.get(id=id)
        selected_data.delete()
        return  redirect ('/customer/customerlist/')
#_________________________________________________________________________________

class customerupdateView(View):
    def get(self,request,id):
        selected_data = customer.objects.get(id=id)
        data = {"custForm":customerForm(instance=selected_data)}
        return render(request,'customeradd.html',data)
    def post(self,request,id):
        selected_data = customer.objects.get(id=id)
        new_data=customerForm(request.POST,instance=selected_data)
        if new_data.is_valid():
            new_data.save()
            return redirect('/customer/customerlist/')
#__________________________________________________________________________________
