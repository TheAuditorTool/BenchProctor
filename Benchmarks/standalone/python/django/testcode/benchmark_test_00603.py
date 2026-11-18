# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00603(request):
    xml_value = request.body.decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
