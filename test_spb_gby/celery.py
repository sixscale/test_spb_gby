import os
from celery import Celery, shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_spb_gby.settings')
app = Celery('test_spb_gby')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.include = ['myapp']
app.autodiscover_tasks()
