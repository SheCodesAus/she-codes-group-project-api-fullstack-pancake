from django.db import models
from django.contrib.auth import get_user_model


# WIP - Not finalised.
class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    workshop_link = models.URLField()
    is_online = models.BooleanField()
    is_in_person = models.BooleanField()
    is_hybrid = models.BooleanField()
    date_and_time = models.DateTimeField()
    organiser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='organiser_workshops'
        # null=True
    )
    # topics = models.CharField(
    #     max_length=200,
    #     choices=[('HTML','HTML'),
    #     ('CSS','CSS'),
    #     ('Python','Python'),
    #     ('Django','Django'),
    #     ('DRF','DRF'),
    #     ('React','React'),
    #     ('PHP','PHP'),
    #     ('AWS','AWS'),
    #     ('Testing','Testing')
    #     ])
    # experience_level = models.enums(
    #     ['Entry-level', 'Intermediate', 'Advanced']
    # )
    # # delivery_method enum
