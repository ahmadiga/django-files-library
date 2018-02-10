from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from django_files_library.models import Library, Permission, File


class BaseSetupTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user("user1", "user1@test.com", "asdasdasd")
        self.user2 = User.objects.create_user("user2", "user2@test.com", "asdasdasd")
        self.user3 = User.objects.create_user("user3", "user3@test.com", "asdasdasd")
        self.user4 = User.objects.create_user("user4", "user4@test.com", "asdasdasd")
        self.public_library = Library.objects.create(name="public library", is_public=True)
        self.private_library = Library.objects.create(name="private library", is_public=False)
        self.permissions1 = Permission.objects.create(user=self.user1, library=self.public_library,
                                                      access_level=Permission.PERMISSION_OWNER)
        Permission.objects.create(user=self.user2, library=self.public_library,
                                  access_level=Permission.PERMISSION_WRITE)
        Permission.objects.create(user=self.user1, library=self.private_library,
                                  access_level=Permission.PERMISSION_OWNER)
        Permission.objects.create(user=self.user2, library=self.private_library,
                                  access_level=Permission.PERMISSION_WRITE)
        Permission.objects.create(user=self.user3, library=self.private_library,
                                  access_level=Permission.PERMISSION_READ)
        self.mock_file = SimpleUploadedFile('best_file_eva.txt', b'these are the file contents!')
        self.file1 = File.objects.create(uploaded_file=self.mock_file, original_name="test file 1",
                                         library=self.public_library,
                                         name="test file 1",
                                         created_by=self.user1)
        self.file2 = File.objects.create(uploaded_file=self.mock_file, original_name="test file 2",
                                         library=self.private_library,
                                         created_by=self.user1)
