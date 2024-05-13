from .forms import LoginForm, CreateUserForm, NewRunRequest
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.db.models.functions import Lower
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from production.models import JobTitle, RunRequest
from users.models import NewUser
import json

# - Home Page
def home(request):
    return render(request, 'app/layout.html')

# - Register a new user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
        
    context = {'form':form}  
    return render(request, 'app/register.html', context = context) 

# - Login an existing user
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    
    context = {'form':form}
    return render(request, 'app/login.html', context=context)

# - Logout a user
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return redirect("login")

# - Dashboard
@login_required(login_url='login')
def dashboard(request):
    # Fetch RunRequest data model
    runs = RunRequest.objects.all()

    # Pass the object to the template context
    context = {
        'runs': runs
    }
    return render(request, 'app/dashboard.html', context=context)

# - Create Run
@login_required(login_url='login')
def new_run(request):
    # Get logged-in user's data
    user = request.user
    requester_name = f"{user.first_name} {user.last_name}"
    requester_phone = user.phone_number
    requester_email = user.email
    requester_department = user.department

    # Create a dictionary with the user data
    initial_data = {
        'requester_name': requester_name,
        'requester_phone': requester_phone,
        'requester_email': requester_email,
        'requester_department': requester_department,
    }

    if request.method == "POST":
        # If it's a POST request, process the form data
        run = NewRunRequest(request.POST)
        if run.is_valid():
            # Process the form data
            run.save()
            return redirect("dashboard")
    else:
        # If it's not a POST request, create a new form instance with initial data
        run = NewRunRequest(initial=initial_data)

    context = {'run': run}
    return render(request, 'app/new_run.html', context=context)

@login_required(login_url='login')
def run_queue(request):
     # Fetch sorted RunRequest queryset
    run_requests = RunRequest.objects.annotate(lower_status=Lower('run_status')).exclude(lower_status__in=['complete', 'cancelled']).order_by('run_date')
    return render(request, 'app/run_queue.html', {'run_requests': run_requests})

@login_required(login_url='login')
def run_history(request):
    # Fetch RunRequest data model
    runs = RunRequest.objects.all()

    # Pass the object to the template context
    context = {
        'runs': runs
    }
    return render(request, 'app/run_history.html', context=context)

@login_required(login_url='login')
def view_run(request, run_request_id):
    run_request = get_object_or_404(RunRequest, id=run_request_id)
    return render(request, 'app/run.html', {'run_request': run_request})
