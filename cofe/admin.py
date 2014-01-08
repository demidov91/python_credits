
from cofe.models import CreditProduct, CreditRequestProcessing, CreditRequestNotes, CreditRequest
from django.contrib import admin




class CreditRequestNotesAdmin(admin.StackedInline):
    model = CreditRequestNotes

class CreditRequestProcessingAdmin(admin.ModelAdmin):
    model = CreditRequestProcessing
    inlines = (CreditRequestNotesAdmin, )

class CreditProductAdmin(admin.ModelAdmin):
    model = CreditProduct
    list_display = ('name', )


admin.site.register(CreditProduct, CreditProductAdmin)
admin.site.register(CreditRequestProcessing, CreditRequestProcessingAdmin)
admin.site.register(CreditRequest)