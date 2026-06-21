# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest68207(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
