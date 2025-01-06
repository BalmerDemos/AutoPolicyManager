from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
import time
import random

# Create your models here.
from django.db import models

COLOR_CHOICES = [
        ('Black', 'Black'),
        ('White', 'White'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Yellow', 'Yellow'),
        ('Silver', 'Silver'),
        # Add more colors here as needed
    ]

# Get the current year dynamically
CURRENT_YEAR = datetime.now().year

# Generate years from 2000 to the current year
YEAR_CHOICES = [(year, str(year)) for year in range(2000, CURRENT_YEAR + 1)]

class Make(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    make = models.ForeignKey(Make, related_name='models', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"

class Car(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default="White")

    @property
    def make(self):
        return self.model.make

    def __str__(self):
        return f"{self.model.year} {self.make.name} {self.model.name}"

class InsurancePolicy(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='insurance')
    policy_number = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    coverage_type = models.CharField(max_length=100)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Policy #{self.policy_number} for {self.car}"

    def clean(self):
        if self.expiration_date <= datetime.now().date():
            raise ValidationError("Expiration date must be in the future.")

    def save(self, *args, **kwargs):
        if not self.policy_number:  # Only generate if it�s not already set (e.g., for new policies)
            self.policy_number = self.generate_policy_number()
        super().save(*args, **kwargs)

    def generate_policy_number(self):
        # Get the current timestamp in seconds (or milliseconds for more precision)
        timestamp = int(time.time() * 1000)  # In milliseconds
        random_number = random.randint(100, 999)  # Random number for more uniqueness
        policy_number = f"POL{timestamp}{random_number}"  # Combine the timestamp and random number
        return policy_number


