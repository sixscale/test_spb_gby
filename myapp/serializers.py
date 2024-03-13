from rest_framework import serializers
from .models import Organization, Event, User


class OrganizationSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Organization
        fields = ['id', 'title', 'description', 'postcode', 'address', 'users', ]


class EventSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'organizations', 'image', 'date']


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField()
    organization = serializers.IntegerField()

    def create(self, validated_data):
        organization_id = validated_data.pop('organization')
        user = User.objects.create_user(**validated_data)

        try:
            organization = Organization.objects.get(id=organization_id)
            organization.users.add(user)
            organization.save()
        except Organization.DoesNotExist:
            pass

        return user

    class Meta:
        model = User
        fields = ('email', 'password', 'phone_number', 'organization')


class EventDetailSerializer(serializers.ModelSerializer):
    organizations = OrganizationSerializer(many=True)

    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'organizations')
