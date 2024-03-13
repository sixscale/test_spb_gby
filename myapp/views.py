from django.shortcuts import render
from django.views import View
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .tasks import create_event_with_delay

from .models import Event, Organization, User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import EventSerializer, OrganizationSerializer, EventDetailSerializer, UserSerializer


class ChatView(View):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, room_name):
        return render(request, 'chat.html', {
            'room_name': room_name
        })


class CustomPaginator(LimitOffsetPagination):
    default_limit = 2


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['date']
    search_fields = ['title', 'description', 'organizations__title', 'organizations__description', ]
    pagination_class = CustomPaginator
    permission_classes = [IsAuthenticated, ]


class EventCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            create_event_with_delay.delay(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        event_serializer = EventDetailSerializer(event)
        return Response(event_serializer.data)


class UserCreateAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            organization_id = serializer.validated_data.pop(
                'organization')
            try:
                organization = Organization.objects.get(id=organization_id)
            except Organization.DoesNotExist:
                return Response({'message': 'Invalid organization ID'}, status=400)

            user = User.objects.create_user(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                phone_number=serializer.validated_data['phone_number']
            )
            organization.users.add(user)
            organization.save()
            return Response({'message': 'User created successfully'})
        else:
            return Response(serializer.errors, status=400)