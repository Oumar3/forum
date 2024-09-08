from django.shortcuts import render
from .models import OfficeForm,EmployeeForm
from django.http import JsonResponse
# Create your views here.
def home(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        'officeForm': officeForm,
        'employeeForm': employeeForm
    }
    return render(request,'ajax/index.html',context)

def officeCRUD(request):
    officeForm = OfficeForm()
    if request.method == 'POST':
        officeForm = OfficeForm(request.POST)
        if officeForm.is_valid():
            officeForm.save()
            return JsonResponse({"message": "Office created successfully!"})

def employeeCRUD(request):
    if request.method == 'POST':
        employeeForm = EmployeeForm(request.POST)
        if employeeForm.is_valid():
            employeeForm.save()
    return JsonResponse({"message": "Employee created successfully!"})