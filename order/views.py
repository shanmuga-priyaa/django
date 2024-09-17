from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import *
from .forms import *

def orderadd(request):
    data = {"OrdForm":OrderForm}
    if request.method == "POST":
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
    return render(request,'orderadd.html',data)
#_____________________________________________________________________________
def orderlist(request):
    data={"orderlist":Order.objects.all()}
    print(data)
    return render(request,'orderlist.html',data)
#_____________________________________________________________________________
def orderdelete(request,id):
    selected_data = Order.objects.get(id=id)
    selected_data.delete()
    return  redirect ('/order/orderlist/')

#_________________________________________________________________________________
def orderupdate(request,id):
     selected_data = Order.objects.get(id=id)
     data = {"OrdForm":OrderForm(instance=selected_data)}

     if request.method == "POST":
         new_data=OrderForm(request.POST,instance=selected_data)
         if new_data.is_valid():
             new_data.save()
             return redirect('/order/orderlist/')

     return render(request,'orderadd.html',data)
#__________________________________________________________________________________
def orderupdate(request,id):
     selected_data = Order.objects.get(id=id)
     data = {"OrdForm":OrderForm(instance=selected_data)}
     if request.method == "POST":
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
     return render (request,'orderadd.html',data)