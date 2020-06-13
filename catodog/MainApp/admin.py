
from django.contrib import admin
from sqlparse.sql import Operation
from .models import Animals
from .models import Transfer

admin.site.register(Animals)
admin.site.register(Transfer)