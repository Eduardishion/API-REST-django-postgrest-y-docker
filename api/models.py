from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=500, null=False)
    brand = models.CharField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
