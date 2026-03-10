from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer, StudentPartialSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    CRUD для студентов.
    GET    /students/          — список (опционально ?course=1..6)
    GET    /students/{id}/     — один студент (404 если не найден)
    POST   /students/          — создать (201)
    PUT    /students/{id}/     — полное обновление
    PATCH  /students/{id}/     — частичное обновление
    DELETE /students/{id}/     — удалить (204)
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        course = self.request.query_params.get('course')
        if course is not None:
            try:
                course = int(course)
                if 1 <= course <= 6:
                    qs = qs.filter(course=course)
            except ValueError:
                pass
        return qs

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return StudentPartialSerializer
        return StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
