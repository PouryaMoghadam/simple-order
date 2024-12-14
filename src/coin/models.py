from django.db import models
from django.utils import timezone


class ActiveCoinManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class Coin(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    last_price = models.DecimalField(max_digits=20, decimal_places=8)
    image = models.ImageField(upload_to="coins/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = ActiveCoinManager()
    all_objects = models.Manager()

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(Coin, self).delete()
