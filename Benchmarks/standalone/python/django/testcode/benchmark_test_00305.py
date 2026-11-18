# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00305(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
