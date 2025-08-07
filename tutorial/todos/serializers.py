from rest_framework import serializers
from .models import Todo, File         # 從Model層引入資料表


class FileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'files', 'uploaded_at', 'todo']


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, allow_blank=True)
    files = FileSerilizer(many=True, read_only=True)
    # 給定資訊
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ('title', 'description', 'is_complete', 'created_time')