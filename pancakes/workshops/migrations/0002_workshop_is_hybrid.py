# Generated by Django 4.0.2 on 2022-09-10 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='is_hybrid',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
