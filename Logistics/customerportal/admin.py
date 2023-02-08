from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Customer)
admin.site.register(Parcel)
admin.site.register(Rider)
admin.site.register(ServiceType)
admin.site.register(Status)
admin.site.register(AssignParcel)
