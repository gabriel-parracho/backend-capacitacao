from rest_framework import serializers
from api.models import Postagem, Comentario, Usuario

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nome','email','is_admin','username','join_date', 'password') #fields = ('id', ...)
        extra_kwargs = {'password': {'write_only': True}}

