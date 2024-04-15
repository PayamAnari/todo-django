from django.db import models
from helpers.models import TrackingModel
from authentication.models import User


class Todo(TrackingModel):

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")

    def __str__(self):
        return self.title
