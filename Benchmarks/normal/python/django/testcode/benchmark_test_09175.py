# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09175(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    eval(str(data))
    return JsonResponse({"saved": True})
