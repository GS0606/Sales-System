from django.db import models


class User (models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document_id = models.CharField(max_length=100, default='default_value')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
