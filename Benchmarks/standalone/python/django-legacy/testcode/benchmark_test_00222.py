# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00222(request):
    xml_value = request.body.decode('utf-8')
    data = ' '.join(str(xml_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
