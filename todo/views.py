from rest_framework.response import Response
from rest_framework import viewsets, serializers, status
from .models import Todo
import time
from silk.profiling.profiler import silk_profile

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @silk_profile(name='Todo List Profiling')
    def list(self, request, *args, **kwargs):
        # Artificial slowness for profiling demo
        _ = list(Todo.objects.all())
        time.sleep(0.1)
        return super().list(request, *args, **kwargs)

    @silk_profile(name='Todo Create Profiling')
    def create(self, request, *args, **kwargs):
        # Intentional ORM slowness: query all todos (unnecessary) & sleep
        _ = list(Todo.objects.all())
        time.sleep(0.2)  # artificial delay

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)