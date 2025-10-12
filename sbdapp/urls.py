from django.urls import path
from .views import contact_view
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path("", views.index_view, name="index"),
    path("interior/", views.interior_view, name="interior"),
    path("sliding/", views.sliding_view, name="sliding"),
    path("construction/", views.construction_view, name="construction"),
    path("contact/", views.contact_view, name="contact"),
]

    