from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['todo_title', 'todo_description', 'is_done', 'uid', 'slug']
        # exclude = ['created_at']

    def get_slug(self, obj):
        return slugify(obj.todo_title)


    def validate_todo_description(self, data): 
        if data:
            todo_description = data

            if len(todo_description) == 0:
                raise serializers.ValidationError('todo description must be added')
        
        return data


    def validate(self, validated_data):
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']

            if len(todo_title) < 3:
                raise serializers.ValidationError('tod title must be more that 3 chars')

            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not (regex.search(todo_title) == None):
                raise serializers.ValidationError('Todo cannot contain special chars')

        return validated_data       