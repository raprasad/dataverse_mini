from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel


class Dataverse(TimeStampedModel):
    name = models.CharField(max_length=255) 
    description = models.TextField()  # used for Dataverse objects?
    
    contact_email = models.EmailField(max_length=255) 

    parent_dataverse = models.ForeignKey('self', blank=True, null=True) 
    
    permissionroot = models.BooleanField(default=False) 
    
    creator = models.ForeignKey(User, blank=True, null=True, related_name='creator')   
 
    publication_date = models.DateTimeField(blank=True, null=True)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='release_user')    

    affiliation = models.CharField(max_length=255, blank=True)
    alias = models.SlugField(max_length=255, blank=True) 
    
    facetroot = models.BooleanField()   
    metadatablockroot = models.BooleanField()   

    md5 = models.CharField(max_length=255, blank=True)  # DataFile

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        

class DataverseProfile(TimeStampedModel):
    dataverse = models.ForeignKey(Dataverse)
    name = models.CharField(max_length=255)
    
    active = models.BooleanField()
    tagline = models.CharField(max_length=255, blank=True)
    
    background_color = models.CharField(max_length=255, blank=True)
    textcolor = models.CharField(max_length=255, blank=True)

    link_color = models.CharField(max_length=255, blank=True)
    link_text = models.CharField(max_length=255, blank=True)
    link_url = models.URLField(max_length=255, blank=True)

    logo = models.CharField(max_length=255, blank=True)
    logo_alignment = models.CharField('Logo Alignment', max_length=255, blank=True)
    logo_background_color = models.CharField('Logo Background Color', max_length=255, blank=True)
    logo_format = models.CharField('Logo Format', max_length=255, blank=True)

    def __unicode__(self):
        return self.dataverse

    class Meta:
        ordering = ('dataverse', 'name',)