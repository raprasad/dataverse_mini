from django.db import models
from django.contrib.auth.models import User

from apps.core.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

class Dataverse(MPTTModel):
    
    name = models.CharField(max_length=255) 
    description = models.TextField()  # used for Dataverse objects?
    
    contact_email = models.EmailField(max_length=255) 

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    permissionroot = models.BooleanField(default=False) 
    
    creator = models.ForeignKey(User, blank=True, null=True, related_name='creator', on_delete=models.PROTECT)   
 
    publication_date = models.DateTimeField(blank=True, null=True)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='release_user', on_delete=models.PROTECT)    

    affiliation = models.CharField(max_length=255, blank=True)
    alias = models.SlugField(max_length=255, blank=True) 
    
    facetroot = models.BooleanField()   
    metadatablockroot = models.BooleanField()   


    created = models.DateTimeField(auto_now_add=True) 
    modified = models.DateTimeField(auto_now=True) 

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        
    class MPTTMeta:
        order_insertion_by = ['name']


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