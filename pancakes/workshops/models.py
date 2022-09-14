from django.db import models
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField

TOPICS = (
    ('HTML','HTML'),
    ('CSS','CSS'),
    ('Python','Python'),
    ('Django','Django'),
    ('JavaScript', 'JavaScript')
    ('DRF','DRF'),
    ('React','React'),
    ('PHP','PHP'),
    ('AWS','AWS'),
    ('Testing','Testing'),
    ('Other', 'Other')
)

EXPERIENCE_LEVEL = (
    ('EL', 'Entry-level'),
    ('INT', 'Intermediate'),
    ('ADV', 'Advanced'),
    ('ALL', 'Everyone')
)

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    workshop_link = models.URLField()
    is_online = models.BooleanField()
    is_in_person = models.BooleanField()
    physical_location = models.CharField(max_length=50, default='Brisbane')
    date_and_time = models.DateTimeField()
    organiser = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='organiser_workshops'
    )
    topics = MultiSelectField(choices=TOPICS, max_choices=11, blank=True)
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=20, default='Entry-level')
