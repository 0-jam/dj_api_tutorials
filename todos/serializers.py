from rest_framework import serializers


class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=40)
    done = serializers.BooleanField(default=False)
