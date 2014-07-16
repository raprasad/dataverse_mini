from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from core.models import TimeStampedModel
from dataverses.models import Dataverse

class Dataset(TimeStampedModel):
    """
    Dataset
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    dataverse = models.ForeignKey(Dataverse)
    
    creator = models.ForeignKey(User, blank=True, null=True, related_name='ds_creator')   
    publication_date = models.DateTimeField(blank=True, null=True)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='ds_release_user')    

    authority = models.CharField(max_length=255, blank=True)    # Dataset, e.g. "10.5072/FK2"
    identifier = models.CharField(max_length=255, blank=True)   # Dataset
    protocol = models.CharField(max_length=255, blank=True)     # Dataset, e.g. "DOI"
    
    
    def __unicode__(self):
        return '%s: %s' % (self.dataverse, self.name)
    
    class Meta:
        ordering = ('name', '-publication_date')
