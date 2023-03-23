from django.shortcuts import get_object_or_404
from rest_framework.decorators import action, permission_classes
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .models import Student, Professor
from .serializers import StudentSerializer, ProfessorSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (student, created) = Student.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        
class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (professor, created) = Professor.objects.get_or_create(
            user_id=request.user.id)
        if request.method == 'GET':
            serializer = ProfessorSerializer(professor)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfessorSerializer(professor, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

