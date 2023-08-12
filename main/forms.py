from .models import Emp_company
from django.forms import ModelForm 
from django import forms

class EmployeeAssociationForm(ModelForm):
    class Meta:
        model = Emp_company
        fields = ['employee']
    
    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        company = cleaned_data.get('company')

        # Check if the employee is already associated with another company
        if Emp_company.objects.filter(employee=employee).exclude(company=company).exists():
            raise forms.ValidationError('This employee is already associated with another company.')

        return cleaned_data