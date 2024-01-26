from django.shortcuts import render
from .serializers import UsuariosSerializer
from .models import Usuarios

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UsuariosView(APIView):
    serializer_class = UsuariosSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        senha = serializer.validated_data.get('senha')

        usuarios = Usuarios.objects.filter(email=email, senha=senha).first()

        if usuarios is None:
            return Response({'message': 'Usuário não encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Usuário encontrado!'}, status=status.HTTP_200_NOT_FOUND)
