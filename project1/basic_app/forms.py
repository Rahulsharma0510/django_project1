from django import forms
from basic_app.models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta():
        model=PersonalInfo
        fields='__all__'
