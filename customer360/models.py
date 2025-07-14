from django.db import models

class Customer(models.Model):
    # Fields (columns for tables)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    # Methods
    def __str__(self):
        return str(self.id)

class Interaction(models.Model):
    # List of Tuples for choices parameter
    # (database_value, object_value)
    CHANNEL_CHOICES = [ # Max char length = 15
        ('phone', 'Phone'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('letter', 'Letter'),
    ]
    DIRECTION_CHOICES = [ # Max char length = 10
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    ]

    # Fields (columns for tables)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    channel = models.CharField(max_length=15, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()