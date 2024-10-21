from django.db import models
import uuid
from django_ckeditor_5.fields import CKEditor5Field
class Bab(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255, verbose_name="اسم الباب", unique=True)
    
    def __str__(self) -> str:
        return self.name
    
class Mawdoe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255, verbose_name="اسم الموضوع", unique=True)
    bab = models.ForeignKey(Bab, on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=255, verbose_name="اسم الصفحة", unique=True)
    mawdoe = models.ForeignKey(Mawdoe, on_delete=models.PROTECT)
    content = CKEditor5Field(verbose_name='محتوى النقطة')
    def __str__(self) -> str:
        return self.name