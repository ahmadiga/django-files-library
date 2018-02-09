import uuid


def unique_file_name(self, file_name):
    """
    Generates Unique name for uploaded filess
    :param self: Filefield object Class
    :param file_name: uploaded file name
    :return: file path with the new filename
    """
    # extract filename and extension
    result = file_name.split('.')
    basename, ext = result[0], '.'.join(result[-1:])
    basename = 'uploads/' + basename
    path, file_actual_name = basename.rsplit('/', 1)
    # Generate new name
    new_name = str(uuid.uuid4())
    file_name = new_name + '.' + ext
    self.original_name = file_actual_name + '.' + ext
    return path + "/" + file_name
