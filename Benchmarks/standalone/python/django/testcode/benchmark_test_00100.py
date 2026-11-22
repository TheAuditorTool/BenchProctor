# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00100(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
