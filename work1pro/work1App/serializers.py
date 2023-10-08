from rest_framework import serializers 
from work1App.models import Dictionary

        

# CRUD
class DictionarySerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=30) 
    description = serializers.CharField(max_length=200)  
    search_count = serializers.IntegerField()    
        
    def create(self, validated_data):
        return Dictionary.objects.create(** validated_data)

    def update(self, instance, validated_data):
        instance.label= validated_data.get('label',instance.label)
        instance.description= validated_data.get('description',instance.description)
        instance.search_count= validated_data.get('search_count',instance.search_count)
        instance.save()
        return  instance









