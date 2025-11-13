from models import *
from rest_framework import serializers

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        field = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        field = '__all__'

class JuegoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Juego
        field = '__all__'