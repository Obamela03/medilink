from django.urls import path
from .views import PrescriptionListCreateView, PrescriptionFulfillView

urlpatterns = [
    path("", PrescriptionListCreateView.as_view(), name="prescriptions"),
    path("<int:pk>/fulfill/", PrescriptionFulfillView.as_view(), name="prescription-fulfill"),
]