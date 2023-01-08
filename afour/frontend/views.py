from django.shortcuts import render, HttpResponse, redirect
from dateutil.relativedelta import relativedelta
import datetime
from backend.models import *
import requests
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import json
from django.http import JsonResponse
from django.core import serializers
import json
from uuid import UUID
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
import re
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
# from .forms import MyfileUploadForm
# from .models import file_upload


# Create your views here.


def home(request):

    return render(request, 'skill.html')


def viewskill(request):
    end_date = datetime.date.today()
    end_date = end_date.strftime("%Y-%m-%d")
    start_date = datetime.date.today() - relativedelta(months=1)
    start_date = start_date.strftime("%Y-%m-%d")

    p = requests.get('http://127.0.0.1:8000/api/skillview/1')
    q = p.json()
    print(q)
    

    # print(q)
    return render(request, 'skill.html', {'b': q, 'frmat': "All", 'end_date': end_date, 'start_date': start_date})


@csrf_exempt
def viewoneskill(request):
    if request.method=="POST":
        q=skill.objects.filter(skill_id=request.POST["id"])
        # print(q)
        data = list(q.values())
        print(data)

       
    return render(request, 'oneskill.html', {'b': data})
def putoneskill(request):
    if request.method == 'POST':
        id = request.POST["id"]
        username = request.POST["username"]
        skill_name = request.POST["skill_name"]
        skill_domain = request.POST["skill_domain"]
        skill_level = request.POST["skill_level"]
        skill_exp = request.POST["skill_exp"]

        context = {
            "username": username,
            "skill_name": skill_name,
            "skill_domain": skill_domain,
            "skill_level": skill_level,
            "skill_exp": skill_exp,

        }
    p=requests.put("http://127.0.0.1:8000/api/skillview/"+id,context)
    print (p)
    return redirect("http://127.0.0.1:8000/viewskill")

def deleteoneskill(request):
    if request.method == 'POST':
        id = request.POST["id"]
        p = requests.delete("http://127.0.0.1:8000/api/skillview/"+id)
    return redirect("http://127.0.0.1:8000/viewskill")


def delete(request, uid):
    member = skill.objects.get(skill_id=uid)
    member.delete()
    return redirect('/viewskill')


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'base.html')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, 'signup.html', context={"register_form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				id=user.id

                
				return redirect('/viewskill')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'login.html', context={"login_form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect('/index')


def addskill(request):
    return render(request,'oneskill.html')

def load_skill(request):
    domain = request.GET.get('skill_domain')
    print(domain)
    
    skills = skill.objects.filter(skill_domain=domain)

    data = {"skills" : skills}

    return render(request,'loadskill.html',data)


def team(request):
    return render(request,'team.html')


def team_list(request):
    domain = request.GET.get('skill_domain')
    name = request.GET.get('skill_name')
    level = request.GET.get('skill_level')
    experience = request.GET.get('skill_experience')

    if level == 'basic':
        data  = skill.objects.filter(skill_domain=domain,skill_name=name,skill_exp__gte=experience).distinct()
    elif level == 'inter':
        data = skill.objects.filter(skill_domain=domain,skill_name=name,skill_exp__gte=experience).exclude(skill_level='basic')
    else:
        data = skill.objects.filter(skill_domain=domain,skill_name=name,skill_level='exp',skill_exp__gte=experience)
    # print(list(data.values()))
        

    return render(request, 'team-list.html', {"b": data})