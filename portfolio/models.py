from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = "projects") # create dir projects on media directori
    created = models.DateTimeField(auto_now_add = True) 
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
            return self.title

    class Meta:

        ordering = ['-created']


        
