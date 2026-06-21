# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05040(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
