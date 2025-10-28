from django.db import models

class Biography(models.Model):
    name = models.CharField(max_length=120)
    occupation = models.CharField(max_length=120, blank=True)
    birth = models.CharField(max_length=120, blank=True)
    death = models.CharField(max_length=120, blank=True)
    nationality = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='biographies/')
    summary = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
