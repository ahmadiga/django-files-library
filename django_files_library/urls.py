from django.conf.urls import url

from django_files_library import views

urlpatterns = [
    url(r'^file/downaload-file/(\d+)/(.+)', views.download_file, name="django_files_library_download_file"),
    url(r'^file/add/(?P<library_id>\d+)/', views.add_file, name="django_files_library_add_file"),
    url(r'^file/delete/(?P<file_id>\d+)/', views.delete_file, name="django_files_library_delete_file"),
]
