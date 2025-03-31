from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  
    Name = serializers.CharField(max_length=30)
    F_name = serializers.CharField(max_length=30)
    M_name = serializers.CharField(max_length=30)
    p_no = serializers.IntegerField()
    course = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    age = serializers.IntegerField()

    def validate_Name(self, value):
        if any(c in "!@#$%^&*()-+?_=,<>/;:[]|" for c in value):
            raise serializers.ValidationError("Name cannot contain special characters")
        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age should be greater than 18")
        return value

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Name = validated_data.get('Name', instance.Name)
        instance.F_name = validated_data.get('F_name', instance.F_name)
        instance.M_name = validated_data.get('M_name', instance.M_name)
        instance.p_no = validated_data.get('p_no', instance.p_no)
        instance.course = validated_data.get('course', instance.course)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
