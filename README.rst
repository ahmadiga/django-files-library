django library

django library is file management django app with user permissions and file download layer


Installation
1. install the package using "pip install git+git://github.com/ahmadiga/django-files-library.git" or "pip install django-files-library"
2. Add "django_library" to your INSTALLED_APPS setting.
3. Add ``` url(r'django_library/', include('django_library.urls')), ``` to urls.py.

Configurations
DJANGO_LIBRARY_ADD_FILE_FORM_CLASS
A string pointing to a custom form class (e.g. ‘myapp.forms.AddFileForm’) that is used during adding new file.

DJANGO_LIBRARY_INLINE_FORM Boolean flag to display upload file form to the list or display it in a separate page

Render library
To render library user the following template tags:
1.```{% render_library <library object> %}```:to render a full view of the library
2.```{% render_library_list <library object> %}```:to render files list only

### TBD