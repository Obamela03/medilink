from django.urls import path
from .views import ConsultationListCreateView

urlpatterns = [
    path("", ConsultationListCreateView.as_view(), name="consultations"),
]