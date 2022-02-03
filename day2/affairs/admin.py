
from django.contrib import admin
from .models import Intake,Students
# Register your models here.
#admin.site.register(Intake)
#admin.site.register(Students,StudentAdmin)
@admin.register(Students)
class StudentAdmin (admin.ModelAdmin):
    fields=(('name','email'),'address')
    list_display=('id','name','email')
    list_filter=('name',)
    search_fields=('name','email')
    ordering=('-name',)
    

@admin.register(Intake)
class IntakeAdmin (admin.ModelAdmin):
    fields=(('name','number'),('start_date','end_date'),'students','manager')
    list_display=('id','name','start_date','end_date','manager')
    list_filter=('number',)
    search_fields=('start_date','end_date')
    ordering=('-number',)