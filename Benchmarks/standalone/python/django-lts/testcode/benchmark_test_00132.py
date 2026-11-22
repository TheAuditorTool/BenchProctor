# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00132(request):
    field_value = request.POST.get('field', '')
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    resp = JsonResponse({'status': 'ok'})
    resp.cookies['session'] = str(data)
    resp.cookies['session'].update({'httponly': True, 'samesite': 'Strict', 'path': '/'})
    return resp
