from rest_framework import serializers

from .models import Task
from django.utils import timezone


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'title': {
                'help_text' : 'Título da tarefa'
            },
            'description': {
                'help_text' : 'Descrição da tarefa'
            },
            'due_date': {
                'help_text' : 'Data de vencimento da tarefa, no formato YYYY-MM-DD'
            },
            'created_at': {
                'help_text' : 'Data de criação da tarefa, no formato YYYY-MM-DD'
            },
            'updated_at': {
                'help_text' : 'Data de atualização da tarefa, no formato YYYY-MM-DD'
            }
        }

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data não pode ser anterior a data atual.")
        return value

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("O campo de título não pode ser vazio.")
        return value
