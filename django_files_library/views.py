from importlib import import_module

from django.core import exceptions
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.encoding import smart_str

from django_files_library import app_settings
from django_files_library.forms import FileForm
from django_files_library.models import File, Library
from django_files_library.templatetags.django_files_library import render_library_list


def download_file(request, pk=None, name=None):
    """
    Download file from library after checking if user have permission to download it
    :param request: 
    :param pk: File primary key
    :param name: File name to be downloaded
    :return: file object if is have permission to read the file or FORBIDDEN if not
    """
    file_obj = File.objects.get(pk=pk)
    try:
        library = file_obj.library
    except:
        return HttpResponse({"message": "Something went wrong! please try again later"}, status=500)

    if library.user_can_read(request.user):
        response = HttpResponse(file_obj.uploaded_file.file, content_type="charset=utf-8")
        response.charset = 'utf-8'
        # response['Content-Length'] = os.path.getsize(settings.BASE_DIR + '/' + file_obj.url())
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_obj.original_name)
        response['Content-Encoding'] = 'utf-8'
        # os.remove(settings.BASE_DIR + '/tmp/' + file_obj.original_name)
        return response
    else:
        return HttpResponseForbidden("You don't have permission to upload to this directory")


def add_file(request, library_id):
    """
    upload and file to library
    :param request: 
    :param library_id: library id to save the file to
    :return: 
    """
    library = get_object_or_404(Library, pk=library_id)
    next_page = request.GET.get("next_url", "/")
    if library.user_can_write(request.user):
        form = get_add_form_class()(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.created_by = request.user
            form.instance.library = library
            form.save()
            if request.is_ajax():
                library.refresh_from_db()
                files_list_html = render_library_list(
                    {"request": request, "next_page": next_page},
                    library)

                result = {"file_list_html": files_list_html}
                return JsonResponse(result)
            else:
                return HttpResponseRedirect(next_page)
        return render(request, "django_files_library/add_file.html", {"form": form, "library": library})
    else:
        return HttpResponseForbidden()


def delete_file(request, file_id):
    """
    Delete file from library
    :param request: 
    :param file_id: file id to be deleted
    :return: 
    """
    file = get_object_or_404(File, pk=file_id)
    next_page = request.GET.get("next_url", "/")
    if file.library.user_can_write(request.user):
        file.delete()
        return HttpResponseRedirect(next_page)
    else:
        return HttpResponseForbidden()


def get_add_form_class():
    """
    get add file form from settings files
    :return: add file form class
    """
    if not app_settings.add_file_form_class:
        form_cls = FileForm
    else:
        try:
            fc_module, fc_classname = app_settings.add_file_form_class.rsplit('.', 1)
        except ValueError:
            raise exceptions.ImproperlyConfigured('%s does not point to a form'
                                                  ' class'
                                                  % app_settings.add_file_form_class)
        try:
            mod = import_module(fc_module)
        except ImportError as e:
            raise exceptions.ImproperlyConfigured('Error importing form class %s:'
                                                  ' "%s"' % (fc_module, e))
        try:
            fc_class = getattr(mod, fc_classname)
        except AttributeError:
            raise exceptions.ImproperlyConfigured('Module "%s" does not define a'
                                                  ' "%s" class' % (fc_module,
                                                                   fc_classname))
        form_cls = fc_class
    return form_cls
