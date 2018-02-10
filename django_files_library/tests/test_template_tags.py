from django.template import Template, Context
from django.test import RequestFactory

from django_files_library.templatetags.django_files_library import render_library, render_library_list
from django_files_library.tests.base_setup import BaseSetupTestCase


class LibraryFormsTestCase(BaseSetupTestCase):
    # Valid Form Data
    def test_render_library(self):
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.user = self.user1
        out = Template(
            "{% load django_files_library %}"
            "{% render_library library %}"
        ).render(Context({"library": self.public_library, "request": request, "csrf_token": ''}))

        expected_html = render_library(
            {"library": self.public_library, "request": request, "csrf_token": ''},
            self.public_library)
        self.assertEqual(out, expected_html)

    def test_render_library_list(self):
        request_factory = RequestFactory()
        request = request_factory.get('/')
        request.user = self.user1
        out = Template(
            "{% load django_files_library %}"
            "{% render_library_list library %}"
        ).render(Context({"library": self.public_library, "request": request, "csrf_token": ''}))

        expected_html = render_library_list(
            {"library": self.public_library, "request": request, "csrf_token": ''},
            self.public_library)
        self.assertEqual(out, expected_html)
