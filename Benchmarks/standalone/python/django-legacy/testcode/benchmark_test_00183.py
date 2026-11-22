# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.parse


def BenchmarkTest00183(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = '%s' % str(json_value)
    encoded_session = urllib.parse.quote(str(data), safe='')
    resp = JsonResponse({'status': 'ok'})
    resp.headers['Set-Cookie'] = 'session=' + encoded_session + '; HttpOnly; SameSite=Strict; Path=/'
    return resp
