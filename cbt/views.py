from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from cbt import forms
from .forms import MyRegistrationForm
from . import models

def accounts(request):
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/accounts.html')

def home(request):
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/home.html')


def login(request):
	c = {}
	c.update(csrf(request))
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/login.html') 

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/cbt/accounts/loggedin')
	else:
		return HttpResponseRedirect('/cbt/accounts/invalid')

def loggedin(request):
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/loggedin.html',{"full_name" : request.user.username})

def invalid_login(request):
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/logout.html')


def register_user(request):
	if request.method == 'POST':
		form = forms.MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/cbt/accounts/register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = forms.MyRegistrationForm()

	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/register.html',args)

"""
def register_user(request):
	if request.method == 'GET':
		form=UserRegistration()
	else:
		form=UserRegistration(request.POST)
		if form.is_valid():
			#uid=form.cleaned_data['userID']
			uname=form.cleaned_data['username']
			emailid=form.cleaned_data['emailID']
			pword=form.cleaned_data['password1']				
			done=models.UserRegistration.objects.create(username=uname,emailID=emailid,password1=pword)
			done.save()
			return HttpResponseRedirect('/cbt/accounts/register_success')
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/register.html',{'form':form})
"""

def register_success(request):
	return render(request,'/home/nikhil/Desktop/CCBT/ccbt/cbt/templates/register_success.html')


