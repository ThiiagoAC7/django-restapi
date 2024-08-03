from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={
            200: 'Tarefa excluída com sucesso.',
            404: 'Tarefa não encontrada'
        }
    )
    def destroy(self, request, *args, **kwargs):
        # instancia do objeto que será excluído
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message":"Task deleted successfully"},
            status=status.HTTP_200_OK)
