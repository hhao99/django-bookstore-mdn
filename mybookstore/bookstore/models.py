from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)

class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    summary = models.TextField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publish_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

