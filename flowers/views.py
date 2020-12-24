from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . import models, forms

class HomeView(ListView):
    model = models.Flower
    paginate_by = 12
    ordering = "-created"
    context_object_name = "flowers"

class FlowerDetail(DetailView):
    model = models.Flower

def search(request):
    flower = request.GET.get("flower")
    flower = str(flower)
    results = models.Flower.objects.filter(name__icontains = flower)
    return render(request, "flowers/search.html", {"flower": flower, "results": results,})

class CreateFlowerView(SuccessMessageMixin, LoginRequiredMixin, FormView):
    login_url = "/users/login/"
    form_class = forms.CreateFlowerForm
    template_name = "flowers/flower_create.html"

    def form_valid(self, form):
        flower = form.save()
        flower.user = self.request.user
        flower.photographer = flower.user
        flower.save()
        return redirect(reverse("flower:detail", kwargs={"pk": flower.pk}))