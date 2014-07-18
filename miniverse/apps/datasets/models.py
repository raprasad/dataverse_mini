from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from apps.core.models import TimeStampedModel
from apps.dataverses.models import Dataverse


class Dataset(TimeStampedModel):
    """
    Dataset
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    dataverse = models.ForeignKey(Dataverse, on_delete=models.PROTECT)
    
    creator = models.ForeignKey(User, blank=True, null=True, related_name='ds_creator', on_delete=models.PROTECT)   
    publication_date = models.DateTimeField(blank=True, null=True)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='ds_release_user', on_delete=models.PROTECT)    

    authority = models.CharField(max_length=255, blank=True)    # Dataset, e.g. "10.5072/FK2"
    identifier = models.CharField(max_length=255, blank=True)   # Dataset
    protocol = models.CharField(max_length=255, blank=True)     # Dataset, e.g. "DOI"
    
    
    def __unicode__(self):
        return '%s: %s' % (self.dataverse, self.name)
    
    class Meta:
        ordering = ('name', '-publication_date')


class DatasetVersion(TimeStampedModel):
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