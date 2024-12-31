from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

# user signup
def signup(request):
    if request.method == 'POST':
       
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Passwords do not match!")

        try:
          
            if User.objects.filter(email=email).exists():
                return HttpResponse("User already exists!")

            # Create and save the new user
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

           
            login(request, user)

           
            return redirect('home')

        except Exception as e:

            return HttpResponse(f"Error: {e}")

   
    return render(request, 'user/signup.html')

# user signin
def signin(request):
    if request.method == 'POST':
   
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
           
            login(request, user)

         
            return redirect('company_dashboard')
        else:

            return HttpResponse("Invalid credentials!,please try again later")

    
    return render(request, 'user/signin.html')

# signout
def signout(request):
    if request.method == 'POST':

        logout(request)

      
        return redirect('signin')

    
    return render(request, 'user/signout.html')
