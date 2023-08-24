from django.contrib import admin
from .models import JuiceTypes, JuiceFruits, JuiceVegetables, JuiceBerries, Package, Services


# Register your models here.
class JuiceTypesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'created',
        'updated',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


class JuiceFruitsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'created',
        'updated',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


class JuiceVegetablesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'created',
        'updated',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)


class JuiceBerriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'created',
        'updated',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)

class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'price',
        'created',
        'updated',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'active',
        'unit',
        'price',
        'created',
        'updated',
    )
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(JuiceTypes, JuiceTypesAdmin)
admin.site.register(JuiceFruits, JuiceFruitsAdmin)
admin.site.register(JuiceVegetables, JuiceVegetablesAdmin)
admin.site.register(JuiceBerries, JuiceBerriesAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Services, ServicesAdmin)