from django.contrib import admin

# Register your models here.

from .models import Apps, Purchases

class PurchasesInline(admin.TabularInline):
    model = Purchases
    extra = 1

class AppsAdmin(admin.ModelAdmin):
    fields = ['app_name', 'app_description', 'app_price']
    list_display = ('app_name', 'app_description', 'app_price')
    
    inlines = [PurchasesInline]
    
    class Meta:
        verbose_name_plural = "Apps"

admin.site.register(Apps, AppsAdmin)
