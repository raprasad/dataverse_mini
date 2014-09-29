from types import NoneType
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel
from apps.datasets.models import Dataset


class MetadataBlock(TimeStampedModel):
    """
    Abstract class implemented by specific Metadata Blocks
    """
    FACETABLE_FIELDS =  None   # () or None, e.g. ('title', 'author', )
    SHOW_ABOVE_FOLD_FIELDS = None
    ADVANCED_SEARCH_FIELDS = None
    
    # blanked out for now
    #dataset_version = models.ForeignKey(DatasetVersion, db_index=True)
    
    # These should be part of the "manager" and abstracted from the content type
    #metadata_block_name = models.CharField(max_length=255, help_text='For display') 
    #metadata_block_description = models.TextField(blank=True)  
    #sort_order = models.IntegerField(default=10)

    def unicode(self):
        return self.metadata_schema_name

    def facetable_fields(self):
        return self.FACETABLE_FIELDS
        
    def validate_chosen_fields(self):
        model_field_names = self._meta.get_all_field_names()
        
        d = {   'FACETABLE_FIELDS':self.FACETABLE_FIELDS\
                , 'SHOW_ABOVE_FOLD_FIELDS':self.SHOW_ABOVE_FOLD_FIELDS\
                , 'SHOW_ABOVE_FOLD_FIELDS':self.ADVANCED_SEARCH_FIELDS\
            }
        for label, field_list in d.items():
            if not type(field_list) in (tuple, NoneType):
                raise Exception('List for %s must be a tuple or None, found type "%s' % (label, type(field_list)))
            if not type(field_list) is tuple: continue
            
            illegal_fields =[f_to_check for f_to_check in field_list if not f_to_check in model_field_names]
            if len(illegal_fields) > 0:
                raise Exception('%s not part of model: %s' % (label, illegal_fields))
        
   
    def save(self, *args, **kwargs):
        self.validate_chosen_fields()
        super(MetadataBlock, self).save(*args, **kwargs)
        
    class Meta:
        ordering = ('sort_order', 'name',)
        abstract = True

'''
class MetadataManager(TimeStampedModel):
    """
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
'''
    
    