from django.contrib import admin

from apps.datasets.models import Dataset, VersionState, DatasetVersion

class DatasetAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['title', 'dataverse__name']
    list_display = ['title',   'dataverse', 'creator', 'created', 'authority', 'identifier', 'protocol']
    list_filter = [ 'dataverse']
    readonly_fields = ['created', 'modified', 'publication_date',]
admin.site.register(Dataset, DatasetAdmin)


class VersionStateAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['name', 'sort_order']
admin.site.register(VersionState, VersionStateAdmin)


class DatasetVersionAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['dataset__title', ]
    list_display = ['dataset',   'version_state', 'semantic_version', 'version_number', 'version_minor_number', ]
    list_filter = [ 'version_state']
    readonly_fields = ['created', 'modified', 'semantic_version',]
admin.site.register(DatasetVersion, DatasetVersionAdmin)

