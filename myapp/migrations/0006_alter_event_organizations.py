# Generated by Django 5.0.3 on 2024-03-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_event_organizations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizations',
            field=models.ManyToManyField(to='myapp.organization'),
        ),
    ]
