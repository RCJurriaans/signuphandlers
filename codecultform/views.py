from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import SummerSchoolSignUp
from .serializers import SignUpSerializer

class SignUpViewSet(viewsets.ModelViewSet):
    queryset = SummerSchoolSignUp.objects.all()
    serializer_class = SignUpSerializer
