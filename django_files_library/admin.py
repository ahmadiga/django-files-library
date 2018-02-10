from django.contrib import admin

from django_files_library.models import Library, Permission, File

admin.site.register(Library)
admin.site.register(Permission)
admin.site.register(File)
