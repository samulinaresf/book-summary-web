from django.db import models 
from accounts.models import Account  
from django.utils import timezone
from datetime import timedelta
 

class Membresia(models.Model):
    
    username = models.OneToOneField(Account, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)  
    date_expired = models.DateTimeField(null=True, blank=True)
    subtotal = models.FloatField(null=True,blank=True)
    tax = models.FloatField(null=True,blank=True)
    total = models.FloatField(null=True,blank=True)
    
    
    def suscripcion_mensual(self):
        self.is_member = True
        self.date_expired = self.date_joined + timedelta(days=30)
        self.subtotal = 4.99
        self.tax = self.subtotal * 0.07
        self.total = self.subtotal + self.tax
        self.save()
        
    def suscripcion_anual(self):
        self.is_member = True
        self.date_expired = self.date_joined + timedelta(days=365)
        self.subtotal = 49.99
        self.tax = self.subtotal * 0.07
        self.total = self.subtotal + self.tax
        self.save()
