from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from . import forms
from .models import Result
from .forms import ResultForm
import requests
import json
# Create your views here.
def myView(request):
    print("Out")
    form=forms.ResultForm()
    if request.method=='POST':
        print("Here")
        global val1,val2
        value1 = request.POST['input1']
        value2 = request.POST['input2']

        if value1 == '':
            val1=0
        else:
            val1=int(value1)
        if value2 == '':
            val2=0
        else:
            val2=int(value2)
        if 'subtract' in request.POST:
            print("sub")
            data1 = {'a': val1, 'b': val2, 'c': 'sub'}
        elif 'add' in request.POST:
            data1 = {'a': val1, 'b': val2, 'c': 'add'}
        else:
            data1 = {'a': val1, 'b': val2, 'c': 'mul'}
        # data1={'a':val1,'b':val2}
        Base_url = 'http://localhost:8000/'
        endpoint = 'api/'
        # if request.POST['subtract']=='subtract':
        #   r = requests.put(Base_url + endpoint, data=json.dumps(data1))
        # elif request.POST['add']:
        #   r = requests.get(Base_url + endpoint, data=json.dumps(data1))
        # else:
        r = requests.get(Base_url + endpoint, data=json.dumps(data1))
        result=r.json()
        print(r.json())

        return render(request, 'TestApp/home.html', {'input1': value1,'input2': value2,'output': result})
    form=ResultForm()
    return render(request,'TestApp/home.html',{'input1': '','input2': '','output': ''})