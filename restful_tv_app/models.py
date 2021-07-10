from django.db import models
import datetime

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        # if str(postData['title']) == str(postData['title']):
        #     errors["title"] = "Title already exist!"
        if len(postData['network']) < 2:
            errors["network"] = "Network should be at least 2 characters"
        # if  (postData['release_date']) > (datetime.date.today()):
        #     errors["release_date"] = "Release date must be in the past"
        if len(postData['description']) <5:
            errors["description"] = "Description should be at least 5 characters"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

