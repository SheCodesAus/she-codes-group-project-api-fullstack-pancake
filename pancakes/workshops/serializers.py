from rest_framework import serializers
from .models import Workshop

class WorkshopSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    workshop_link = serializers.URLField()
    is_online = serializers.BooleanField()
    is_in_person = serializers.BooleanField()
    date_and_time = serializers.DateTimeField()
    organiser = serializers.ReadOnlyField(source='organiser.id')
    # topics = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Workshop.objects.create(**validated_data)

class WorkshopDetailSerializer(WorkshopSerializer):

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.workshop_link = validated_data.get('workshop_link', instance.workshop_link)
        instance.is_online = validated_data.get('is_online', instance.is_online)
        instance.is_in_person = validated_data.get('is_in_person', instance.is_in_person)
        instance.date_and_time = validated_data.get('date_and_time', instance.date_and_time)
        instance.organiser = validated_data.get('organiser', instance.organiser)
        # instance.topics = validated_data.get('topics', instance.topics)
        instance.save()
        return instance