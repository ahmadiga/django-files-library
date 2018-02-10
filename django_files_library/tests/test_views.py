import io

from django.urls import reverse

from django_files_library.tests.base_setup import BaseSetupTestCase


class LibraryviewsTestCase(BaseSetupTestCase):
    def test_download_file_user1_view(self):
        user_login = self.client.login(email=self.user1.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file1.pk, self.file1.name)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file2.pk, self.file2.name)))
        self.assertEqual(response.status_code, 200)

    def test_download_file_user2_view(self):
        user_login = self.client.login(email=self.user2.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file1.pk, self.file1.name)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file2.pk, self.file2.name)))
        self.assertEqual(response.status_code, 403)

    def test_download_file_user3_view(self):
        user_login = self.client.login(email=self.user3.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file1.pk, self.file1.name)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file2.pk, self.file2.name)))
        self.assertEqual(response.status_code, 200)

    def test_download_file_user4_view(self):
        user_login = self.client.login(email=self.user4.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file1.pk, self.file1.name)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("django_files_library_download_file", args=(self.file2.pk, self.file2.name)))
        self.assertEqual(response.status_code, 403)

    def test_add_file_user1_view(self):
        user_login = self.client.login(email=self.user1.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 200)

    def test_add_file_user2_view(self):
        user_login = self.client.login(email=self.user2.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 200)

    def test_add_file_user3_view(self):
        user_login = self.client.login(email=self.user3.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 403)

    def test_add_file_user4_view(self):
        user_login = self.client.login(email=self.user4.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}))
        self.assertEqual(response.status_code, 403)

    def test_add_file_user1_success_post_view(self):
        user_login = self.client.login(email=self.user1.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.post(
            reverse("django_files_library_add_file", kwargs={"library_id": self.public_library.pk}),
            data={'name': "test", 'description': "test desc",
                  'uploaded_file': (io.BytesIO(b'hi everyone'), 'test.csv')})
        self.assertEqual(response.status_code, 302)

    def test_delete_file_user3_view(self):
        user_login = self.client.login(email=self.user3.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_delete_file", kwargs={"file_id": self.file1.pk}))
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse("django_files_library_delete_file", kwargs={"file_id": self.file2.pk}))
        self.assertEqual(response.status_code, 403)

    def test_delete_file_user4_view(self):
        user_login = self.client.login(email=self.user4.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_delete_file", kwargs={"file_id": self.file1.pk}))
        self.assertEqual(response.status_code, 403)
        response = self.client.get(
            reverse("django_files_library_delete_file", kwargs={"file_id": self.file2.pk}))
        self.assertEqual(response.status_code, 403)

    def test_delete_file_user1_view(self):
        user_login = self.client.login(email=self.user1.email, password="asdasdasd")
        self.assertTrue(user_login)
        response = self.client.get(
            reverse("django_files_library_delete_file", kwargs={"file_id": self.file1.pk}))
        self.assertEqual(response.status_code, 302)
