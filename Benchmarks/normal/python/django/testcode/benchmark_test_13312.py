# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13312(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
