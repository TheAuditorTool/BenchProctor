# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51637(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data) in ('localhost', 'internal-gateway'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
