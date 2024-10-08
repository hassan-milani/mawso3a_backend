from django.db import models
from django.contrib.auth.models import Permission, User
import uuid
# Create your models here.


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=100, verbose_name="الصلاحية", unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    
    def __str__(self) -> str:
        return self.name


class UserProfile(models.Model):
    id = models.UUIDField(verbose_name="الرمز التعريفي", default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles")
    name = models.CharField(max_length=255, verbose_name="اسم المستخدم")
    roles = models.ManyToManyField(Role, verbose_name="الصلاحية", blank=True)
    info = models.TextField(verbose_name="معلومات اضافية عن المستخدم", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def has_role(self, role_name):
        return self.roles.filter(name=role_name).exists()

    def has_permission(self, perm_name):
        return self.roles.filter(permissions__codename=perm_name).exists()
    
