from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Recipe)
admin.site.register(models.Feedback)
admin.site.register(models.Subcategory)
admin.site.register(models.Category)