# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest56218(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(json_value), secure=True, httponly=True, samesite='Strict')
    return resp
