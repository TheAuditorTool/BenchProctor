# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import importlib


def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

def BenchmarkTest00090(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ' '.join(parts)
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
