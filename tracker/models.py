from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100)       # Name of the expense
    amount = models.FloatField()                    # Amount spent
    category = models.CharField(max_length=50)     # Category like Food, Travel
    date = models.DateField()                       # Date of expense
    description = models.TextField(blank=True, null=True)  # Optional note

    def __str__(self):
        return f"{self.title} - {self.amount}"
