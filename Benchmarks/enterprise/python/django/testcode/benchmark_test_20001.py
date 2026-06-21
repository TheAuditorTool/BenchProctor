# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20001(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        int(str(data))
    except ValueError:
        return JsonResponse({'error': 'invalid'}, status=400)
    return JsonResponse({"saved": True})
