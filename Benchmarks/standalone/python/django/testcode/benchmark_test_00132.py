# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00132(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = ' '.join(str(json_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
