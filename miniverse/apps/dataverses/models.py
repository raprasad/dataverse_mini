from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

from model_utils.models import TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey

class Dataverse(MPTTModel):
    """
    Basic dataverse object
    """
    name = models.CharField(max_length=255) 
    description = models.TextField()  # used for Dataverse objects?
    
    contact_email = models.EmailField(max_length=255) 

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    
    permissionroot = models.BooleanField(default=False) 
    
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.PROTECT)
 
    publication_date = models.DateTimeField(blank=True, null=True)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='release_user', on_delete=models.PROTECT)
    affiliation = models.CharField(max_length=255)
    alias = models.SlugField(max_length=255, blank=True, help_text='auto-filled on save')
    
    facetroot = models.BooleanField(default=False)
    metadatablockroot = models.BooleanField(default=False)

    permission_root = models.BooleanField(default=False)
    template_root = models.BooleanField(default=False)

    #default_template = models.

    display_by_type = models.BooleanField(default=False)
    display_feature = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True) 
    modified = models.DateTimeField(auto_now=True) 

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        self.alias = slugify(self.name)
        super(Dataverse, self).save(*args, **kwargs)


    class Meta:
        ordering = ('name',)
        permissions = (
                    ("publish_dataverse", "Can publish dataverse"),
#                    ("change_task_status", "Can change the status of tasks"),
#                    ("close_task", "Can remove a task by setting its status as closed"),
                )
                
    class MPTTMeta:
        order_insertion_by = ['name']


class DataverseProfile(TimeStampedModel):
    """
    Customize the look/feel of a dataverse
    """
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