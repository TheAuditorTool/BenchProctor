# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.parse


def BenchmarkTest00047(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; Secure; HttpOnly; SameSite=Strict; Path=/'
    return resp
