# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00183(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
