from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models


def get_object_or_none(Class: models.Model, pk: str):
    try:
        item = Class.objects.get(pk=pk)
    except (ObjectDoesNotExist, ValidationError):
        return None
    return item
