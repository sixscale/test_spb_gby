from test_spb_gby.celery import shared_task
from time import sleep
from .serializers import EventSerializer


@shared_task
def create_event_with_delay(event_data):
    sleep(60)
    serializer = EventSerializer(data=event_data)
    if serializer.is_valid():
        serializer.save()
