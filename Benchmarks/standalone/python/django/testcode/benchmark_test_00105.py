# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.parse


def BenchmarkTest00105(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
