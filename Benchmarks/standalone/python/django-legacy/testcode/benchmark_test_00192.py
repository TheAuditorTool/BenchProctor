# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00192(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
