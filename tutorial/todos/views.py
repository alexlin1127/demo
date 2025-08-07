from rest_framework import viewsets
from .models import Todo, File
from .serializers import TodoSerializer, FileSerilizer
from rest_framework import status
from rest_framework.response import Response
from django_filters import rest_framework as filter
from rest_framework.permissions import IsAuthenticated

# django-filter 專門用來處理Django REST Framework的過濾功能
class TodoFilter(filter.FilterSet):
    class Meta:
        model = Todo
        fields = ('title',)

class TodoViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset =  Todo.objects.all().order_by('-created_time')   # 定義 viewset，找資料庫以及他如何回傳給前端
    serializer_class = TodoSerializer  # 將序列化層綁訂到這個 viewset
    filterset_class = TodoFilter       # 將過濾器綁訂到這個 viewset
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        request_data = request.data
        # request_data['title'] = f'python_course_{request_data['title']}'
        
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerilizer
    permission_classes = [IsAuthenticated]