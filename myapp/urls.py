from django.urls import path
from myapp import views


urlpatterns = [
    path('ws/chat/<str:room_name>/', views.ChatView.as_view()),
    path('all/', views.EventListAPIView.as_view()),
    path('create-event/', views.EventCreateAPIView.as_view()),
    path('create-organization/', views.OrganizationCreateAPIView.as_view()),
    path('create-user/', views.UserCreateAPIView.as_view()),
    path('events/<int:event_id>/', views.EventDetailAPIView.as_view(), name='event_detail'),
]
