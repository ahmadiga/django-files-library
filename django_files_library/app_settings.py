class AppSettings(object):
    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        from django.conf import settings
        getter = getattr(settings,
                         'ALLAUTH_SETTING_GETTER',
                         lambda name, dflt: getattr(settings, name, dflt))
        return getter(self.prefix + name, dflt)

    @property
    def ADD_FILE_FORM_CLASS(self):
        """
        Add file form
        """
        return self._setting("ADD_FILE_FORM_CLASS", None)

    @property
    def INLINE_FORM(self):
        """
        Add file form
        """
        return self._setting("INLINE_FORM", False)


# Ugly? Guido recommends this himself ...
# http://mail.python.org/pipermail/python-ideas/2012-May/014969.html
import sys  # noqa

app_settings = AppSettings('DJANGO_FILES_LIBRARY_')
app_settings.__name__ = __name__
sys.modules[__name__] = app_settings
