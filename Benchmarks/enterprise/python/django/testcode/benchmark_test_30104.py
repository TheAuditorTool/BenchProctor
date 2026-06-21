# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest30104(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = FormData(payload=host_value).payload
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
