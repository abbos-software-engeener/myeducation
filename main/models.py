from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    excel_product = models.FileField(upload_to="uploads/excel")

    class Meta:
        verbose_name = "Mahsulohlar Excel Fayli "
        verbose_name_plural = "Mahsulohlar Excel Fayllari "

@receiver(post_save, sender=Order)
def bitrix(sender, instance: Order, created, **kwargs):
    if not created:
        from main import helpers
        helpers.more_adding_warehouse_product(instance)

class Product(models.Model):
    excel_product = models.FileField(upload_to="uploads/excel")
    product_id = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveSmallIntegerField(default=0,blank=True)
    tags = models.CharField(max_length=100,blank=True)
    image_url = models.URLField(blank=True)
    option_Name = models.CharField(max_length=200,blank=True)
    hidden = models.CharField(max_length=200,blank=True)
    weight = models.CharField(max_length=200,blank=True)
    prepaymentPercent = models.CharField(max_length=200,blank=True)
    bonusesPercent = models.CharField(max_length=200,blank=True)
    hidden_btn = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['product_id']



