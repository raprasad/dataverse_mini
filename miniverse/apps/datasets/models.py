from os.path import join

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from model_utils.models import TimeStampedModel
from apps.dataverses.models import Dataverse
#from apps.metadata_citations.models import CitationBlock

class Dataset(TimeStampedModel):
    """
    Basic Dataset object.
    Except for title, citation metadata is stored in other areas
    """
    dataverse = models.ForeignKey(Dataverse, on_delete=models.PROTECT)

    title = models.CharField(max_length=255, db_index=True)

    publication_date = models.DateTimeField(blank=True, null=True)

    creator = models.ForeignKey(User, related_name='ds_creator', on_delete=models.PROTECT)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='ds_release_user', on_delete=models.PROTECT)

    authority = models.CharField(max_length=255, default='10.5072/FK2')    #  e.g. "10.5072/FK2"
    identifier = models.IntegerField(default=-1)
    protocol = models.CharField(max_length=255, default='doi')     # e.g. "DOI"

    def __unicode__(self):
        return '%s: %s' % (self.dataverse, self.title)

    def save(self, *args, **kwargs):
        self.identifier = self.id   # for now...
        super(Dataset, self).save(*args, **kwargs)


    def get_partial_path_for_datafile(self):
        return join(self.authority, self.identifier)

    class Meta:
        ordering = ('title', '-publication_date')


class VersionState(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    sort_order = models.IntegerField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('sort_order', 'name')
    #DRAFT, IN_REVIEW, RELEASED, ARCHIVED, DEACCESSIONED

    
class DatasetVersion(TimeStampedModel):

    dataset = models.ForeignKey(Dataset)
    
    version_state = models.ForeignKey(VersionState)
    
    version_number = models.IntegerField()
    version_minor_number = models.IntegerField()
    
    semantic_version = models.CharField(max_length=50, blank=True, help_text='auto-filled on save')
    
    #citation_block = models.ForeignKey(CitationBlock)
    
    deaccessionLink = models.URLField(blank=True)
    
    archive_note = models.TextField(max_length=1000, blank=True)
    archive_time = models.DateTimeField(blank=True, null=True)
    

    def __unicode__(self):
        return '%s; v. %s' % (self.dataset, self.semantic_version)


    def save(self, *args, **kwargs):
        self.semantic_version = '%s.%s' % (self.version_number, self.version_minor_number)
        super(DatasetVersion, self).save(*args, **kwargs)
    
    
    """
    title
    version_state       # #DRAFT, IN_REVIEW, RELEASED, ARCHIVED, DEACCESSIONED
    
    version_number
    minor_version_number
    
    private Date releaseTime;
    private Date archiveTime;
    private String archiveNote;
    private String deaccessionLink;
    md5
    
    
    getMostRecentlyReleasedVersion
    getLargestMinorRelease
    is_latest_version
    getDatasetAuthors
    getCitation
    
    public String getSemanticVersion() {
           
            if (this.isReleased()){
                return versionNumber + "." + minorVersionNumber;
            } else {
                return "DRAFT";
            }        
        }
"""