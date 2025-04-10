from django.db import models

# Create your models here.
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('completed', 'Завершено'),
        ('cancelled', 'Отменено'),
    ]

    user = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка {self.id} от {self.user}"