from django.db import models

from model_utils.models import TimeStampedModel
from apps.metadata_block.models import MetadataBlock

class CitationSubject(TimeStampedModel):
    name = models.CharField(max_length=255)
    
    def unicode(self):
        return self.name
    
    class Meta:
        ordering = ('name', )

class CitationAuthor(TimeStampedModel):
    name = models.CharField(max_length=255, help_text='The person(s), corporate body(ies), or agency(ies) responsible for creating the work.')
    
    def unicode(self):
        return '%s, %s' % (self.last_name, self.first_name)
    
    class Meta:
        ordering = ('name', )

class DistributorContact(TimeStampedModel):
    
    email = models.EmailField()

    def unicode(self):
        return self.email
    
    class Meta:
        ordering = ('email',)
    
class CitationBlock(MetadataBlock):

    # Define facetable fields, show above fold fields, and advanced search fields
    # These fields name are validated when an object is saved
    FACETABLE_FIELDS = ('authorName', 'authorAffiliation', )
    SHOW_ABOVE_FOLD_FIELDS = ('title', 'authorName', 'authorAffiliation', 'distributorContact', 'dsDescription')
    ADVANCED_SEARCH_FIELDS = ('title', 'authorName', 'distributorContact')
    
    
    title = models.CharField(max_length=255, help_text="Full title by which the Dataset is known.")
    author = models.ManyToManyField(CitationAuthor, blank=True, null=True)
    authorName = models.CharField(max_length=255, help_text="The author's Family Name, Given Name or the name of the organization responsible for this dataset.")
    authorAffiliation = models.CharField(max_length=255, blank=True, help_text="The organization with which the author is affiliated.")
    distributorContact = models.ManyToManyField(DistributorContact)
    dsDescription = models.TextField(help_text="A summary describing the purpose, nature, and scope of the Dataset.")
    subject = models.ManyToManyField(CitationSubject)

    def unicode(self):
        return self.title

    class Meta:
        ordering = ('title', )
        verbose_name = 'Citation Block'
        #facetable = ('title', 'authorName')
        
    
"""
    keyword = models.ManyToManyField(blank=True, null=True)
    notesText = models.TextField(blank=True, help_text="Additional important information about the Dataset")
    otherId = models.ManyToManyField(blank=True, null=True)
    otherIdValue = models.CharField(max_length=255, blank=True, help_text="Other identifier that corresponds to this Dataset.")
    otherIdAgency = models.CharField(max_length=255, blank=True, help_text="Name of agency which generated this identifier.")
    publication = models.ManyToManyField(blank=True, null=True)
    publicationCitation = models.TextField(blank=True, help_text="The full bibliographic citation for this related publication.")
    publicationIDType = models.CharField(max_length=255, blank=True, help_text="The type of digital identifier used for this publication (max_length=255e.g., Digital Object Identifier (max_length=255DOI)).")
    publicationIDNumber = models.CharField(max_length=255, blank=True, help_text="The identifier for the selected ID type.")
    publicationURL = models.URLField(blank=True, help_text="Link to the publication web page (e.g., journal article page, archive record page, or other).")
    contributor = models.ManyToManyField(blank=True, null=True)
    contributorType = models.CharField(max_length=255, blank=True, help_text="The type of contributor of the  resource.  ")
    contributorName = models.CharField(max_length=255, blank=True, help_text="The Family Name, Given Name or organization name of the contributor.")
    contributorAffiliation = models.CharField(max_length=255, blank=True, help_text="The organization which the contributor is affiliated with.")
    contributorAbbreviation = models.CharField(max_length=255, blank=True, help_text="The abbreviation by which the contributor's affiliation is commonly known (max_length=255e.g., IQSS, ICPSR, etc).")
    productionDate = models.DateField(blank=True, help_text="Date when the data collection or other materials were produced (not distributed, released or archived).")
    productionPlace = models.CharField(max_length=255, blank=True, help_text="The location where the data collection and any other related materials were produced.")
    grantNumber = models.ManyToManyField(blank=True, null=True)
    grantNumberValue = models.CharField(max_length=255, blank=True, help_text="The grant or contract number of the project that  sponsored the effort.")
    grantNumberAgency = models.CharField(max_length=255, blank=True, help_text="Grant Number Agency")
    depositor = models.CharField(max_length=255, blank=True, help_text="The person (max_length=255Family Name, Given Name) or the name of the organization that deposited this Dataset to the repository.")
    dateOfDeposit = models.DateField(blank=True, help_text="Date that the Dataset was deposited into the repository.")
    relatedMaterial = models.ManyToManyField(blank=True, null=True)
    relatedDatasets = models.ManyToManyField(blank=True, null=True)
    otherReferences = models.ManyToManyField(blank=True, null=True)
    """