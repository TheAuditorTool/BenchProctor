# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.parse


def BenchmarkTest00061(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ' '.join(parts)
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
