# Generated by Django 4.0.2 on 2022-09-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_profile_image_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.CharField(default='/pancakes/images/Dandelion.png', max_length=200),
        ),
    ]