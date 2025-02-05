from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from home.forms import CreateAccountForm, LoginForm

def home(request):
    page_data = {
        "shooters" : [
            {"player1":"Stephen Curry", "team1":"Golden State Warriors", "stat1":"43%"},
			{"player2":"Klay Thompson", "team2":"Golden State Warriors", "stat2":"39%"},
        ],
		"defenders" : [
			{"player1":"Ben Simmons", "team1":"Philadelphia 76ers", "stat1":"2.6 blocks and 2.7 fouls"},
			{"player2":"Rudy Gobert", "team2":"Utah Jazz", "stat2":"2.5 blocks and 2.5 fouls"},
		],
    }
    return render(request, 'home/home.html', page_data)

def create_account(request):
    if request.method == "POST":
        account_form = CreateAccountForm(request.POST)
        if (account_form.is_valid()):
            user = account_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = { "account_form": account_form }
            return render(request, 'home/create-account.html', page_data)
    else:
        account_form = CreateAccountForm()
        page_data = { "account_form": account_form }
        return render(request, 'home/create-account.html', page_data)

def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                return render(request, 'home/login.html', {"login_form": LoginForm})
    else:
        return render(request, 'home/login.html', {"login_form": LoginForm})

def logout_user(request):
    logout(request)
    return redirect("/")