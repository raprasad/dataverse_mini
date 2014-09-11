from django.contrib import admin

from apps.datafiles.models import DataFile

class DataFileAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['title', 'dataverse__name']
    list_display = ['dataset',  'ingest_status', 'content_type'\
                    , 'file_system_name', 'file_size']
    list_filter = [ 'dataset']
    readonly_fields = ['file_size', 'created', 'modified', ]
admin.site.register(DataFile, DataFileAdmin)

