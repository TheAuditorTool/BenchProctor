# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00098(request):
    cookie_value = request.COOKIES.get('session_token', '')
    form = FormData(payload=cookie_value)
    data = form.payload
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
