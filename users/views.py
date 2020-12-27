from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms, models

class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("flower:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(username=email, password=password)
        # Request가 1번째 인자였는데 뺐음.
        if user is not None:
            messages.success(self.request, "안녕하세요!")
            login(self.request, user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    messages.info(request, "안녕히 가세요!")
    return redirect(reverse("flower:home"))

class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("flower:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            messages.success(self.request, "환영합니다!")
            login(self.request, user)
        return super().form_valid(form)