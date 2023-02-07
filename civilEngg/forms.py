from django import forms
from civilEngg.models import Students

class StudentsModelForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'
