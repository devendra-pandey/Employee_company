from django.shortcuts import render , redirect
from django.http import HttpResponse
from main.models import Company , Employee , Emp_company
from .forms import EmployeeAssociationForm
from django.forms import ModelForm
# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all()})

def add_employee(request, company_id):
    company = Company.objects.get(pk=company_id)
    employee = Employee.objects.all()
    if request.method == 'POST':
        form = EmployeeAssociationForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            Emp_company.objects.create(company=company, employee=employee)
            return redirect('/')
    else:
        form = EmployeeAssociationForm()

    return render(request, 'add_employee.html', {'form': form, 'company': company ,'employee':employee})