from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from django_files_library.forms import FileForm


class LibraryFormsTestCase(TestCase):
    # Valid Form Data
    def test_fileform_valid(self):
        mock_file = SimpleUploadedFile('best_file_eva.txt', b'these are the file contents!')
        form = FileForm(data={'name': "test", 'description': "test desc", 'uploaded_file': mock_file},
                        files={'uploaded_file': mock_file})
        self.assertTrue(form.is_valid())

        # Invalid Form Data

    def test_fileform_invalid(self):
        form = FileForm(
            data={'name': "test", 'description': "test desc", 'first_name': "user", 'uploaded_file': None})
        self.assertFalse(form.is_valid())
