from os.path import basename, join

from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

from model_utils.models import TimeStampedModel

from apps.datasets.models import Dataset
from apps.utils.uuid_service import generate_storage_identifier

INGEST_STATUS_NONE = 1
INGEST_STATUS_SCHEDULED = 2
INGEST_STATUS_IN_PROGRESS = 3
INGEST_STATUS_ERROR = 4
INGEST_CHOICES_LIST = (INGEST_STATUS_NONE, INGEST_STATUS_SCHEDULED, INGEST_STATUS_IN_PROGRESS, INGEST_STATUS_ERROR)
INGEST_CHOICES  = [ (x, x) for x in INGEST_CHOICES_LIST]

dv_file_system_storage = FileSystemStorage(location=settings.DV_DATAFILE_DIRECTORY)

def generate_new_filename(instance, filename):
    #f, ext = os.path.splitext(filename)

    return join(instance.dataset.get_partial_path_for_datafile(), generate_storage_identifier())

class DataFile(TimeStampedModel):

    """
    Basic Dataset object.
    Except for title, citation metadata is stored in other areas
    """
    dataset = models.ForeignKey(Dataset, on_delete=models.PROTECT)

    content_type = models.CharField(max_length=255, db_index=True)

    file_obj = models.FileField(upload_to=generate_new_filename\
                            , storage=dv_file_system_storage)# max_length=255)

    file_system_name = models.CharField(max_length=255, blank=True, help_text='(auto-filled on save)')
    file_size = models.BigIntegerField('File size (in bytes)', default=-1, help_text='(auto-filled on save)')

    #ingest_status = Choices('none', 'scheduled', 'in progress', 'error')
    ingest_status = models.IntegerField(choices=INGEST_CHOICES, default=INGEST_STATUS_NONE)

    creator = models.ForeignKey(User, blank=True, null=True, related_name='df_creator', on_delete=models.PROTECT)
    release_user = models.ForeignKey(User, blank=True, null=True, related_name='df_release_user', on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.file_size = self.file_obj.size
        #self.file_system_name = basename(self.file_obj.name)
        super(DataFile, self).save(*args, **kwargs)


    def __unicode__(self):
        return '%s: %s' % (self.dataset, self.file_system_name)

    class Meta:
        ordering = ('dataset', 'file_system_name')


@receiver(post_save, sender=DataFile, dispatch_uid='set_filename_to_uuid')
def update_file_system_name(sender, **kwargs):
    datafile_obj = kwargs.get('instance', None)
    if type(datafile_obj) is not DataFile:
        return
    DataFile.objects.filter(id=datafile_obj.id\
                    ).update(\
                        file_system_name=basename(datafile_obj.file_obj.name)\
                    )
