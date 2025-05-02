from django.db import models

# Create your models here.
# translator/models.py

class Translation(models.Model):
    kurukh_text = models.TextField()
    hindi_translation = models.TextField()

    def __str__(self):
        return self.kurukh_text
