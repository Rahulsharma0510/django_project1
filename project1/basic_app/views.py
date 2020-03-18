from django.shortcuts import render
from django.http import HttpResponse
from basic_app.models import PersonalInfo
from basic_app.forms import PersonalInfoForm
# Create your views here.

def index1(request):
    form = PersonalInfoForm()

    if request.method =='POST':
        form = PersonalInfoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index2(request)
        else:
            print("Error")

    return render(request,'basic_app/form_model.html',{'form':form})


def index2(request):
    return render(request,'basic_app/thank_you.html')

def index3(request):
    return render(request,'basic_app/base.html')


def index4(request):
    return render(request,'basic_app/capestone.html')
