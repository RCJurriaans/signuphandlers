from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from .models import SummerSchoolSignUp
from .serializers import SignUpSerializer

class SignUpViewSet(generics.CreateAPIView):
    queryset = SummerSchoolSignUp.objects.all()
    serializer_class = SignUpSerializer
