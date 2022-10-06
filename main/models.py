from django.db import models


class Order(models.Model):
    excel_product = models.FileField(upload_to="uploads/excel")

    class Meta:
        verbose_name = "Mahsulohlar Excel Fayli "
        verbose_name_plural = "Mahsulohlar Excel Fayllari "


class Product(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    option_Name = models.CharField(max_length=200, null=True, blank=True)
    hidden = models.CharField(max_length=200, null=True, blank=True)
    weight = models.CharField(max_length=200, null=True, blank=True)
    prepaymentPercent = models.CharField(max_length=200, null=True, blank=True)
    bonusesPercent = models.CharField(max_length=200, null=True, blank=True)
    hidden_btn = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['product_id']
