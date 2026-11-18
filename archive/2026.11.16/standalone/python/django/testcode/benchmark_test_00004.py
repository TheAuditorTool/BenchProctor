# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00004(request):
    xml_value = request.body.decode('utf-8')
    kind = 'json' if str(xml_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(xml_value).strip()
        case _:
            data = str(xml_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
