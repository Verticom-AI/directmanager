from django.db import models
from client.models import User


class Ticket_subject(models.Model):
    subject = models.CharField(max_length=50, verbose_name='عنوان')
    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوعات'
    def __str__(self) -> str:
        return self.subject
    
    
class Message(models.Model):
    sender           = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    receiver         = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='receiver')
    content          = models.TextField(blank=True)
    media_content    = models.FileField(upload_to='messages/media_content/', blank=True)
    date             = models.DateTimeField(auto_now_add=True)
    is_read          = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
    def __str__(self) -> str:
        return self.content
class Ticket(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مشتری')
    subject = models.ForeignKey('Ticket_subject', on_delete=models.CASCADE, verbose_name='موضوع')
    started_date = models.DateTimeField(auto_now_add=True)
    messages = models.ManyToManyField('Message')
    STATUS_CHOICES = (
        (1,'نیازمند پاسخگویی'),
        (0,'پاسخ داده شده')
    )
    status = models.BooleanField(choices=STATUS_CHOICES,default=1, verbose_name='وضعیت تیکت')
    refered = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin', null=True, blank=True, verbose_name='ارجاع')
    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'
    def __str__(self) -> str:
        return self.client.username
    
