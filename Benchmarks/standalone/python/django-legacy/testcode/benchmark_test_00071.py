# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00071(request):
    user_id = request.GET.get('id', '')
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(user_id)
    resp.cookies['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
