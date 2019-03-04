from django.db import models

# Create your models here.


class Language(models.Model): 
    language = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.language


class Project(models.Model):
    title = models.CharField(max_length=128, blank=False)
    modal_title = models.CharField(max_length=128, blank=False)
    language = models.ForeignKey(Language, on_delete=True)
    img_source = models.URLField(blank=False)
    info = models.TextField(blank=False)
    gif = models.URLField(blank=False)
    github = models.URLField(blank=False)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.title
