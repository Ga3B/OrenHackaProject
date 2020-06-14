
from django.contrib import admin
from sqlparse.sql import Operation
from .models import *

admin.site.register(Animals)
admin.site.register(Transfer)
admin.site.register(Animal_status)
admin.site.register(Status)
admin.site.register(Request)
admin.site.register(Shelter)
