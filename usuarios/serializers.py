from rest_framework import serializers

class UsuariosSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    senha = serializers.CharField(max_length=100)
