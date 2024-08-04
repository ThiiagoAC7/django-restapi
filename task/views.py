from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(responce_body=TaskSerializer)
    def list(self, request):
        title = request.GET.get('title', None)
        due_date = request.GET.get('due_date', None)
        _queryset = self.queryset 
        if title:
            _queryset = Task.objects.filter(title=title)  
        if due_date:
            _queryset= Task.objects.filter(due_date=due_date)

        serializer = self.serializer_class(_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responce_body=TaskSerializer)
    def retrieve(self, request):
        # instancia do objeto que será retornado
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responce_body=TaskSerializer)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responce_body=TaskSerializer)
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responce_body=TaskSerializer)
    def destroy(self, request, pk=None):
        # instancia do objeto que será excluído
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message":"Task deleted successfully"},
            status=status.HTTP_200_OK)
