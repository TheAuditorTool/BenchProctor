# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest10471(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
