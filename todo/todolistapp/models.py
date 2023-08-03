from django.db import models

# Create your models here.
class Todo(models.Model): # converts the normal class into model class
    status_choice = [('Done', 'Done'), ('Not done', 'Not done')]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=status_choice)

    def __str__(self) : #to change the representor of object
        return self.title