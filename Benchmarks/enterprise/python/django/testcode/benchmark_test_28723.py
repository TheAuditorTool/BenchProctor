# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest28723(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    pending = list(str(ua_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.seteuid(65534)
    return JsonResponse({"saved": True})
