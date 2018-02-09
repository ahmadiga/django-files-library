from django.forms import ModelForm

from django_library.models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['name', 'description', 'uploaded_file']
