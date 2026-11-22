# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'
def _revive_typed(fields):
    type_name = fields.pop('__type__', None)
    if type_name is None:
        return fields
    module_name, _, class_name = type_name.rpartition('.')
    return getattr(importlib.import_module(module_name), class_name)(**fields)

def BenchmarkTest00126(request):
    cookie_value = request.COOKIES.get('session_token', '')
    form = FormData(payload=cookie_value)
    data = form.payload
    parsed = json.JSONDecoder(object_hook=_revive_typed).decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
