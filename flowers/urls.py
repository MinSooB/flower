from django.urls import path
from . import views

app_name = "flower"

urlpatterns = [
    path("create/", views.CreateFlowerView.as_view(), name="create"),
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.FlowerDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditFlowerView.as_view(), name="edit"),
    path("search/", views.search, name="search")
]
