from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)
    click_count = models.IntegerField(default=0)  # <-- add default
