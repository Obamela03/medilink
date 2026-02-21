from django.urls import path
from .views_doctors import DoctorListView

urlpatterns = [
    path("", DoctorListView.as_view()),
]