# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def ensure_str(value):
    return str(value)

def BenchmarkTest49839(request):
    xml_value = request.body.decode('utf-8')
    data = ensure_str(xml_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
