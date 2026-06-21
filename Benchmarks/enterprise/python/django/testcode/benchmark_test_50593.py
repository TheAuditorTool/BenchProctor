# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50593(request):
    host_value = request.META.get('HTTP_HOST', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
