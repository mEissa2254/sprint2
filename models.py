from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=20)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()
    max_participants = models.PositiveIntegerField()
    event_status = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
def _str_(self):
    return self.name
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    role = models.TextField()
    phone_number = models.BigIntegerField()
    profile_picture = models.ImageField(upload_to='photos/%y/%m/%d')
    nationality = models.CharField(max_length=100)



    def __str__(self):
        return self.email


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
        ('cryptocurrency', 'Cryptocurrency'),
        ('gift_card', 'Gift Card'),
        ('mobile_payment', 'Mobile Payment'),
    ]
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_status = models.CharField(max_length=100)
    is_confirmed = models.BooleanField(default=False)

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('success', 'Success'),
    ]
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

     

     




     



