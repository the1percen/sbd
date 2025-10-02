from django.urls import path
from .views import contact_view
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("interior/", views.interior_view, name="interior"),
    path("sliding/", views.sliding_view, name="sliding"),
    path("contact/", views.contact_view, name="contact"),
]
