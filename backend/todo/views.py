from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

class TodoList(APIView):

	def get(self, request):
		todo = Todo.objects.all()
		serializer = TodoSerializer(todo, many=True)
		return Response(serializer.data)

	def post(self):
		pass	