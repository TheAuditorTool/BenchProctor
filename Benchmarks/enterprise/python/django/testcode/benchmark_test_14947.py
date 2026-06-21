# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest14947(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return JsonResponse({"saved": True})
