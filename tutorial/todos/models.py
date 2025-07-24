from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=32)
    kind = models.CharField(max_length=16, null=True)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class File(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='files')
    files = models.FileField(upload_to='todo_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'File for {self.todo.title}'