# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest09641(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = FormData(payload=host_value).payload
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
