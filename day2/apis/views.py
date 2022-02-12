from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from affairs.models import Students
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

@api_view(['PUT', 'DELETE'])
def student_details(request, pk):

    student = get_object_or_404(Students,pk=pk)
 
    if request.method == 'PUT':
        serializer = UserSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)