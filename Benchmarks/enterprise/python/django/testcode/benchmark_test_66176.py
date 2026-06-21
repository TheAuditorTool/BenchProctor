# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest66176(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
