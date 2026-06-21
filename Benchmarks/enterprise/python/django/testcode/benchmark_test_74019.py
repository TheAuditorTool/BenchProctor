# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest74019(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
