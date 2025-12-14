from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms import SignUpForm  # важно, чтобы "F" была большой

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("flats:flats_list")  # имя URL главной страницы
    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})
