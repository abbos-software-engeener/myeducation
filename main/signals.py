from django.db.models.signals import post_save
from django.dispatch import receiver
#
# from main.helpers import more_adding_warehouse_product
# from main.models import Order
#
#
# @receiver(post_save, sender=Order)
# def bitrix(sender, instance: Order, created, **kwargs):
#     if not created:
#
#         more_adding_warehouse_product(instance)
