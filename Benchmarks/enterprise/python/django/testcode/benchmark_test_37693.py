# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest37693(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = str(json_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
