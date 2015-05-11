from django.contrib.auth.models import User, Group
from codecultform.models import SummerSchoolSignUp
from rest_framework import serializers


class SignUpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SummerSchoolSignUp
        fields = ('name', 'email', 'age', 'city', 'message', 'parent')
