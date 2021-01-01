from django.urls import path
from . import views

app_name = "flower"

urlpatterns = [
    path("create/", views.CreateFlowerView.as_view(), name="create"),
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.FlowerDetail.as_view(), name="detail"),
    path("<int:pk>/edit/", views.EditFlowerView.as_view(), name="edit"),
    path("<int:pk>/delete/", views.delete_photo, name="delete"),
    path("flower/", views.FlowerView.as_view(), name="c_flower"),
    path("family/", views.FamilyView.as_view(), name="c_family"),
    path("others/", views.OthersView.as_view(), name="c_others"),
    path("search/", views.search, name="search")
]
