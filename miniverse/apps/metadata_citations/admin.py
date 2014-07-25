from django.contrib import admin

from apps.metadata_citations.models import *
# Register your models here.
admin.site.register(CitationSubject)
admin.site.register(CitationAuthor)
admin.site.register(DistributorContact)
admin.site.register(CitationBlock)