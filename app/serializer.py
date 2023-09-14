from rest_framework import serializers
from .models import student



class studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=50)
    
    def create(self,validate_data):
        return student.objects.create(**validate_data)
        
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)   
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    def validate(self, attrs):
        rol=attrs.get('roll')
        if rol>=200:
            raise serializers.ValidationError('roll must be less than 200')
        return attrs