from django.contrib import admin
from ticket import models


admin.site.register(models.Ticket)
admin.site.register(models.Message)
admin.site.register(models.Ticket_subject)