# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest54558(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
