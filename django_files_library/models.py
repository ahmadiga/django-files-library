from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from django_files_library.tools import unique_file_name


class Library(models.Model):
    display_fields = ["name"]
    name = models.CharField(max_length=255, null=True, blank=True)
    is_public = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Created On"))

    def user_can_read(self, user):
        return self.is_public or self.permission_set.filter(
            Q(Q(user=user) & Q(Q(access_level="O") | Q(access_level="R")))).exists()

    def user_can_write(self, user):
        return self.permission_set.filter(
            Q(Q(user=user) & Q(Q(access_level="O") | Q(access_level="W")))).exists()

    def __str__(self):
        return self.name


class Permission(models.Model):
    PERMISSION_READ = 'R'
    PERMISSION_WRITE = 'W'
    PERMISSION_OWNER = 'O'

    PERMISSION_CHOICES = (
        (PERMISSION_READ, "Read"),
        (PERMISSION_WRITE, "Write",),
        (PERMISSION_OWNER, "Owner",)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Created On"))
    access_level = models.CharField(max_length=1, choices=PERMISSION_CHOICES)

    def __str__(self):
        return self.library.name + ' - ' + self.user.username


class File(models.Model):
    uploaded_file = models.FileField(upload_to=unique_file_name)
    original_name = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_("Created On"))
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def url(self):
        return self.uploaded_file.url.split('?')[0]
