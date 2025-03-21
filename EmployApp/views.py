from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeForm
from .models import Employee
from django.shortcuts import render


# Create your views here.
def HomePage(request):
    form = EmployeForm()  # Initialize form outside of if block
    if request.method == "POST":
        form = EmployeForm(request.POST)
        if form.is_valid():  # Always check if form is valid before saving
            form.save()
            form = EmployeForm()  # Reset form after saving
    
    employees = Employee.objects.all()  # Fetch all employee records

    context = {
        'form': form,
        'employees': employees  # Updated variable to match template
    }
    return render(request, 'EmployApp/index.html', context)


def Update(request, id):
    user = get_object_or_404(Employee, id=id)  # Use get_object_or_404 for safety

    if request.method == "POST":
        form = EmployeForm(request.POST, instance=user)  # Correct form initialization
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after update
    
    else:
        form = EmployeForm(instance=user)  # Use correct form variable

    context = {
        'form': form,
        'user': user  # Added user to context for additional template usage
    }
    return render(request, 'EmployApp/update.html', context)


def Delete_record(request, id):
    user = get_object_or_404(Employee, id=id)  # Use get_object_or_404 for safety
    user.delete()
    return redirect('home')


def AboutUS(request):
    return render(request, 'EmployApp/about.html')


def Services(request):
    return render(request, 'EmployApp/services.html')


def chat_view(request):
    return render(request, 'chatbot.html')