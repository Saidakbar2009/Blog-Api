from rest_framework.serializers import ModelSerializer
from .models import *

class MuallifModelSerializer(ModelSerializer):
    class Meta:
        model = Muallif
        fields = '__all__'

class MaqolaModelSerializer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'