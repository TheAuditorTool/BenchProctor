# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import urllib.parse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00009(request):
    user_id = request.GET.get('id', '')
    form = FormData(payload=user_id)
    data = form.payload
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
