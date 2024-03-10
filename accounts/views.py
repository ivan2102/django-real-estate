from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contacts


def dashboard(request):
    user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
       'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

def register(request):
    if request.method == 'POST':
      #form value
       first_name = request.POST['first_name'] 
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       confirm_password = request.POST['confirm_password']

       #Validation
       if password == confirm_password:
        #Check if username exists in database
          if User.objects.filter(username=username).exists():
             messages.error(request, 'Username already exists')
             return redirect('register')
          
          else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('register')
            else:
              user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
              user.save()
              messages.success(request, 'Your registration has been  successful')
              return redirect('login')
       else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
     return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
           auth.login(request, user)
           messages.success(request, 'You are successfully logged in')
           return redirect('dashboard')
        
        else:
           messages.error(request, 'Invalid credentials')
           return redirect('login')
    else:
     return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       return redirect('login')
    
