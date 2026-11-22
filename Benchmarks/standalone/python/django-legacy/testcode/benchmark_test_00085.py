# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00085(request):
    host_value = request.META.get('HTTP_HOST', '')
    form = FormData(payload=host_value)
    data = form.payload
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
