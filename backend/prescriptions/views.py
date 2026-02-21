from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PrescriptionListCreateView(APIView):
    def get(self, request):
        return Response({"results": [], "message": "Prescriptions list (stub)"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"detail": "Not implemented yet"}, status=status.HTTP_501_NOT_IMPLEMENTED)

class PrescriptionFulfillView(APIView):
    def patch(self, request, pk):
        return Response({"detail": "Not implemented yet"}, status=status.HTTP_501_NOT_IMPLEMENTED)