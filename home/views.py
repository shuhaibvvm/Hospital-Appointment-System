from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors
from .form import BookingForm





# Create your views here.
def index(request):
    numbers = {
        'fruits': ['apple','orange','beans','banana']
    }
    return render(request, 'index.html', numbers)

def about(request):
    return render(request, 'about.html')


def booking(request):
    form = BookingForm(request.POST or None)  # Pass request.POST data if it's a POST request
    
    # Handle form submission
    if request.method == 'POST' and form.is_valid():
        form.save()  # Save the form data to the database
        # You can add additional actions here, such as redirecting to a success page
    
    context = {
        'form': form
    }
    
    return render(request, 'booking.html', context)



def doctors(request):
    dic_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dic_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

