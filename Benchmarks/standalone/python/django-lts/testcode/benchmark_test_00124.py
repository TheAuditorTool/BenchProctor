# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00124(request):
    field_value = request.POST.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
