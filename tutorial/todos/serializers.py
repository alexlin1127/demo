from rest_framework import serializers
from .models import Todo # 從Model層引入資料表


class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    # 給定資訊
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ('title', 'description', 'is_complete', 'created_time')
        