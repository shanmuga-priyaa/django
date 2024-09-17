from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import * 

def loginpage(request):
    if request.method == 'POST':
        print(request.POST)
        user_data = authenticate(username=request.POST['username'], password= request.POST['password'])
        print(user_data)

        if user_data is not None:
            login(request,user_data)
            return redirect ('/product/productlist/')
        else:
            msg={"error":"Invalid username or password"}
            return render(request,'loginpage.html',msg)
        
    return render(request,'loginpage.html')

def logoutpage(request):
    logout(request)
    return redirect('/')

def signuppage(request):
    if request.method == 'POST':
        print(request.POST)
        # Extracting user information from the POST request
        email = request.POST['email']
        full_name = request.POST['fullname']
        phone = request.POST['phone']
        password = request.POST['password']
        
        # Create a new user
        try:
            user = User.objects.create_user(username=email, password=password)
            user.first_name = full_name
            user.email = email
            user.save()
            # Automatically log the user in after sign up
            login(request, user)
            
            # Redirect to the product list or another page
            return redirect('/product/productlist/')
        
        except Exception as e:
            # Handle the error (e.g., user already exists)
            msg = {"error": "Failed to create an account. Please try again."}
            return render(request, 'Signup.html', msg)
        
#______________________________________________________________________________________
def signuppage(request):
    if request.method == 'POST':
        user_check = User_details.objects.filter(username=request.POST['username'])
        print(user_check)
        if len(user_check)>0:
           msg = {"error": "Username already exists"}
           return render(request,"Signup.html",msg)
        else:
            new_user = User_details(username = request.POST['username'],
                                first_name = request.POST['first name'],
                                last_name = request.POST['last name'],
                                mobile_number = request.POST['mobile number'],
                                address = request.POST['address'],
                                age = request.POST['age']
                                )
        new_user.set_password(request.POST['password']) 
        new_user.save()
        return redirect("/")
    return render(request, 'Signup.html')

 