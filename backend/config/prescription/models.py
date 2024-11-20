from django.db import models
from client.models import User
from store.models import Product


class Prescript(models.Model):
    consultant = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='consultant_prescript')
    client     = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='client_prescript')
    drugs = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'نسخه'
        verbose_name_plural = 'نسخه ها'
    
    def __str__(self):
        return self.consultant.username
