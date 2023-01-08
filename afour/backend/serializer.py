from rest_framework import serializers
from .models import *

class skillSerializer(serializers.ModelSerializer):
    class Meta:
        model=skill
        fields='__all__'