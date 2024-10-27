from rest_framework import serializers

from .models import Computer, Software

class ComputerSerializer(serializers.ModelSerializer):
    softwares = serializers.SerializerMethodField()
    class Meta:
        model = Computer
        fields = '__all__'