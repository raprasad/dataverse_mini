from django.contrib import admin
from dataverses.models import Dataverse, DataverseProfile

class DataverseAdmin(admin.ModelAdmin):

    save_on_top = True
    search_fields = []
    list_display = ['id',   'name', 'parent_dataverse', 'created',]
    list_filter = [ 'parent_dataverse']   
    readonly_fields = ['created', 'md5', 'modified', 'publication_date',]
    fieldsets = [
        ('Dataverse', {
           'fields': ('name'\
           , 'contact_email'\
            , 'description'\
            , 'parent_dataverse'\
            , 'affiliation'\
            , 'alias'\
            , 'facetroot'\
            , 'permissionroot'\
            , 'metadatablockroot')
         }),
       
         ('Creator', { \
            'fields' : ('creator', )\
         }),
        
         ('Publication', { \
            'fields' : ('publication_date', 'release_user' )\
         }),
        ('Read-only Fields', {\
            'fields': ( 'created', 'modified', )
        }),
       ]


admin.site.register(Dataverse, DataverseAdmin)

admin.site.register(DataverseProfile)   #, DataverseProfileAdmin)

"""
  ('Dataverse Styling', {
              'fields': ('tagline'\
                , 'textcolor'\
                , 'background_color'\
                , 'link_color'\
                , 'link_text'\
                , 'link_url'\
                , 'logo'\
                , 'logo_alignment'\
                , 'logo_background_color'\
                , 'logo_format'\
                 )
   }),
"""
