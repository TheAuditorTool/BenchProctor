# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02919(request):
    host_value = request.META.get('HTTP_HOST', '')
    pending = list(str(host_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
