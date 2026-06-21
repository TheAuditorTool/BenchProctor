# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest27148(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
