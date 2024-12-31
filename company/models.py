from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):

    """

    Model to store the details of company.

    :attributes:
        - user: id for user the created the company
        - name: name of the company
        - address: address of the company
        - contact_number: contact of the company

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
