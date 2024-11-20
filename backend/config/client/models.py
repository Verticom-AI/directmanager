from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class User(AbstractUser):
    fullname = models.CharField(max_length=40)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    avatar = models.ImageField(default='client/profile/avatar/default_avatar.png', upload_to='profile/avatar/', blank=True)
    consultant = models.BooleanField(default=False)
    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'