# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest22377(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
