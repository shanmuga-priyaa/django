from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import *
from .forms import *
from django.views import View



class orderaddview(View):
    def get(self,request):
        data = {"OrdForm":OrderForm}
        return render(request,'orderadd.html',data)
    def post(self,request):
        data = {"OrdForm":OrderForm}
        sp = Product.objects.get(id=request.POST['product_ref'])
        pro_price = float(request.POST['quantity'])*sp.price
        pro_gst = (pro_price*sp.gst)/100
        pro_FP = pro_price + pro_gst
        new_order=Order(product_ref_id =request.POST['product_ref'],
                        customer_ref_id=request.POST['customer_ref'],
                        order_data  =request.POST['order_data'],
                        quantity    =request.POST['quantity'],
                        price       =pro_price,
                        gst         =pro_gst,
                        final_price =pro_FP,
                        )
        new_order.save()
        return redirect ('/order/orderlist/')
#_____________________________________________________________________________

class orderlistView(View):
    def get(self,request):
        data={"orderlist":Order.objects.all()}
        print(data)
        return render(request,'orderlist.html',data)
#_____________________________________________________________________________

class orderdeleteview(View):
    def get(self,request,id):
        selected_data = Order.objects.get(id=id)
        selected_data.delete()
        return  redirect ('/order/orderlist/')
    

#__________________________________________________________________________________

class orderupdateview(View):
    def get(self,request,id):
        selected_data = Order.objects.get(id=id)
        data = {"OrdForm":OrderForm(instance=selected_data)}
        return render(request,'orderadd.html',data)
    def post(self,request,id):
        sp = Product.objects.get(id=request.POST['product_ref'])
        pro_price = float(request.POST['quantity'])*sp.price
        pro_gst = (pro_price*sp.gst)/100
        pro_FP = pro_price + pro_gst
        update_row = Order.objects.filter(id=id)
        update_row.update(product_ref_id =request.POST['product_ref'],
                          customer_ref_id=request.POST['customer_ref'],
                          order_data  =request.POST['order_data'],
                          quantity    =request.POST['quantity'],
                          price       =pro_price,
                          gst         =pro_gst,
                          final_price =pro_FP,)
        return redirect ('/order/orderlist/')
        