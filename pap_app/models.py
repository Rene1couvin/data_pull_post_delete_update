# models.py

from django.db import models
from datetime import datetime

def generate_id():
    current_date = datetime.now().strftime("%y%m%d")
    last_entry = DataModel.objects.last()
    if last_entry:
        last_id = int(last_entry.unique_id[-4:]) + 1
        return f"{current_date}{str(last_id).zfill(4)}"
    else:
        return f"{current_date}0001"

class DataModel(models.Model):
    unique_id = models.CharField(max_length=12, default=generate_id, unique=True, editable=False)
    picture = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    age = models.IntegerField()
    dob = models.DateField()
    id_number = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
