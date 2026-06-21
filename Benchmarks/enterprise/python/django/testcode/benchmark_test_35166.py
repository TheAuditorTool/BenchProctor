# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest35166(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
