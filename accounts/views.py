from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup(request):

	if request.method == 'POST' :
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)

			return redirect('articles:list')
	else :
		form = UserCreationForm()

	return render(request,'accounts/signup.html',{'form':form})


def login_(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			# login the user
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next')) 
			return redirect('articles:list')

	else :
		form = AuthenticationForm()
	return render(request,'accounts/login.html',{'form':form})

def logout_(request):
	if request.method == 'POST':
		logout(request)
	return redirect('articles:list')