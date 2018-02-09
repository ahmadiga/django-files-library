from django.conf.urls import url

from django_library import views

urlpatterns = [
    url(r'^file/downaload-file/(\d+)/(.+)', views.download_file, name="django_library_download_file"),
    url(r'^file/add/(?P<library_id>\d+)/', views.add_file, name="django_library_add_file"),
    url(r'^file/delete/(?P<file_id>\d+)/', views.delete_file, name="django_library_delete_file"),
]
