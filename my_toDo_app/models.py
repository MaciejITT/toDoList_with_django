from django.db import models
# Create your models here.


class Todo(models.Model):
    added_date = models.DateTimeField()
    item_todo = models.CharField(max_length=200)

    def __str__(self):
        return self.item_todo
