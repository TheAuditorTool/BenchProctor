# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00116(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'secure': True, 'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
