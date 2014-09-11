from django.contrib import admin

from apps.datasets.models import Dataset

class DatasetAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['title', 'dataverse__name']
    list_display = ['title',   'dataverse', 'creator', 'created', 'authority', 'identifier', 'protocol']
    list_filter = [ 'dataverse']
    readonly_fields = ['created', 'modified', 'publication_date',]
admin.site.register(Dataset, DatasetAdmin)

