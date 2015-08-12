from django.db import models

# Create your models here.

class Apps(models.Model):
    app_name = models.CharField(max_length=200)
    app_description = models.CharField(max_length=1000)
    app_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)


class Purchases(models.Model):
    purchased_app = models.ForeignKey(Apps)
    user = models.CharField(max_length=200)
    purchase_date = models.DateTimeField('date purchased')
    