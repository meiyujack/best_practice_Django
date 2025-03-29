from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display=("lastname","firstname","phone","joined_date")
    prepopulated_fields={"slug":("lastname","firstname")}

admin.site.register(Member,MemberAdmin)
