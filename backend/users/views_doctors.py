from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class DoctorListView(APIView):
    def get(self, request):
        doctors = User.objects.filter(role="doctor").values("id", "username", "email")
        return Response({"results": list(doctors)}, status=status.HTTP_200_OK)