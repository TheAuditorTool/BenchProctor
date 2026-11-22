# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.parse


def BenchmarkTest00102(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; Secure; HttpOnly; SameSite=Strict; Path=/'
    return resp
