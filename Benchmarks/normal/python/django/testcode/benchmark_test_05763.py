# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest05763(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})
