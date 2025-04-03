from django.db import models


class Bag(models.Model):
    kind = models.PositiveBigIntegerField(unique=True)


class Order(models.Model):
    blended_at = models.DateTimeField(null=True, default=None)
    gross_weight = models.FloatField(null=True, default=None)
    tare_weight = models.FloatField(null=True, default=None)
    total_tons = models.FloatField(null=True, default=None)
    blend_status = models.CharField(max_length=2, blank=True)
    bag_type = models.ForeignKey(Bag, on_delete=models.CASCADE, null=True)



