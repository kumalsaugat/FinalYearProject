from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from StudentEvaluation.forms import DataForm



def homepage(request):
    return render(request, "homepage.html")

def form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index_view')
        else:
            print('Form is invalid:', form.errors)
    else:
        form = DataForm()
    context = {
        'form':form,
    }
    return render(request, "form.html", context)


def register_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not User.objects.filter(username=username).exists():
            
            try:
                user_obj = User.objects.create(username=username)
                user_obj.password = make_password(password=password1)
                user_obj.save()

                messages.success(request, 'Your Account is Created. Now you can Login')
                return redirect('login_view')

            except Exception as e:
                print(e)

        else:
            messages.success(request, 'Try Another Username')
            return redirect('register_view')

    context = {}
    return render(request, 'register.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You Have Successfully Logged In.')
                return redirect('index_view')

            else:
                messages.success(request, 'Type Correct Credentails')
                return redirect('register_view')

        except Exception as e:
            print(e)

    context = {}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('register_view')



from StudentEvaluation.models import Profile

MARITAL_STATUS = {

    1: 'Single',
    2:  'Married' ,
    3:  'Widower' ,
    4:  'Divorced' ,
    5:  'Facto union'  ,
    6:  'Legally separated' ,
}

def index_view(request):

    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
        profile = None
        print('Exception : ', e)

    
    context = {
        'profile': profile,
        'MARITAL_STATUS' : MARITAL_STATUS,
    }
    return render(request, 'index.html', context)
