# Generated by Django 4.0.2 on 2022-08-30 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_remove_workshop_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='organiser',
        ),
    ]
