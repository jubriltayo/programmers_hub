from django.db import models


class Tip(models.Model):
    LANGUAGES = [
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Java', 'Java'),
        ('C++', 'C++'),
    ]

    tipId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    language = models.CharField(max_length=50, choices=LANGUAGES)
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    