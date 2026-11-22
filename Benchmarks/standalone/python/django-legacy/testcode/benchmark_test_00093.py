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

def BenchmarkTest00093(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value if xml_value else 'default'
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
