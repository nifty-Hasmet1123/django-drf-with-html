from typing import Type, AnyStr
from django.db import models
from django.db.models import Max

DJANGO_MODEL = Type[models.Model]

def generate_unique_id(
    model_class: DJANGO_MODEL, 
    field_name: AnyStr, 
    prefix: AnyStr
):
    """
    Generates a unique ID with the given prefix for the specified model and field.
    Example: AST-0001, DPT-0001
    """
    
    if not hasattr(model_class, field_name):
        raise AttributeError(f"{ model_class.__name__ } has no field named '{field_name}'") 

    last_id = model_class.objects.aggregate(Max(field_name))[f"{field_name}__max"]
    
    new_number = 1
    if last_id:
        try:
            last_number = int(
                str(last_id).split("-")[-1]
            )
            new_number = last_number + 1
        except (IndexError, ValueError):
            pass # Keep new_number as 1 if parsing fails
    
    return f"{prefix}-{new_number:04d}"