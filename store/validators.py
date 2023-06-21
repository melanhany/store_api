from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_kb = 500

    if file.size > max_size_kb * 1024:
        raise ValidationError(f'The maximum size of image is {max_size_kb}')