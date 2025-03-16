from rest_framework import serializers
from .models import Contact , Esports

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class EsportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esports
        fields = '__all__'