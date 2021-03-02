from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=40)
    done = models.BooleanField(default=False)


class TodoListItem(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    title = models.CharField(max_length=40)
    done = models.BooleanField(default=False)
