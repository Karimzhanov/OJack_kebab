from django.contrib import admin
from apps.contacts.models import Contacts, Contact, Reservation, Reservatio

# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'email']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']

@admin.register(Reservatio)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', ]