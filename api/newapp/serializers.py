from rest_framework import serializers,fields
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name','is_staff')
        extra_kwargs = {
            'last_login': {'read_only': True},
        }

    def create(self, validated_data):

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.save()
        return user


class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Incidents
        fields = '__all__'

class MotivationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Motivation
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):

    # userId = serializers.SlugRelatedField(
    #     slug_field='email',
    #     queryset=models.UserProfile.objects.all(),)

    class Meta:
        model = models.Detail
        fields = '__all__'

class TransportsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.Transports
        fields = '__all__'


class TypeIncidentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.TypeIncidents
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = models.Group
        fields = '__all__'

class PeriodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Periode
        fields = '__all__'