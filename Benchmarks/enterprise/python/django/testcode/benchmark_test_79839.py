# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79839(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    exec(str(data))
    return JsonResponse({"saved": True})
