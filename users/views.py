from django.shortcuts import redirect, render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
# from django.urls import reverse

# Create your views here.
def logout_view(request):
    """Logging Out the user"""
    logout(request)
    return redirect('topics:home_page')

def register(request):
    """Register a new user"""



    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save() # save the form to the database
            print(new_user)
            print(request.POST)
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return redirect('topics:topics_list')

    return render(request,'users/register.html',{'form':form})