from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.shortcuts import render, reverse, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    success_message = "저장 완료"

    def form_valid(self, form):
        flower = form.save()
        flower.user = self.request.user
        flower.photographer = flower.user
        flower.save()
        return redirect(reverse("flower:detail", kwargs={"pk": flower.pk}))
    
class EditFlowerView(SuccessMessageMixin, UpdateView):
    model = models.Flower
    form_class = forms.EditFlowerForm
    template_name = "flowers/flower_edit.html"
    success_message = "수정 완료!"

@login_required
def delete_photo(request, pk):
    user = request.user
    
    flower = models.Flower.objects.get(pk=pk)
    if flower.photographer.pk != user.pk:
        messages.error(request, "삭제할 수 없음!")
    else:
        models.Flower.objects.filter(pk=pk).delete()
        messages.success(request, "삭제 완료!")
    return redirect(reverse("flower:home"))

class FlowerView(ListView):
    queryset = models.Flower.objects.all()
    queryset = queryset.filter(classification = "Flower")
    paginate_by = 12
    ordering = "-created"
    context_object_name = "flowers"

class FamilyView(ListView):
    queryset = models.Flower.objects.all()
    queryset = queryset.filter(classification = "Family")
    paginate_by = 12
    ordering = "-created"
    context_object_name = "flowers"

class OthersView(ListView):
    queryset = models.Flower.objects.all()
    queryset = queryset.filter(classification = "Others")
    paginate_by = 12
    ordering = "-created"
    context_object_name = "flowers"