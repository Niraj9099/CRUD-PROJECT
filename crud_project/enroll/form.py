from django import forms
from .models import Student

class StudentRegister(forms.ModelForm):
    error_css_class = "errors"
    class Meta:
        model = Student
        # fields = ['name', 'email', 'password']
        fields = '__all__'
        # exclude = ['password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }