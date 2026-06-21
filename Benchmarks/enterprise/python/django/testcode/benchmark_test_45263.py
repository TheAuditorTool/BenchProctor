# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45263(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    pending = list(str(header_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    eval(str(data))
    return JsonResponse({"saved": True})
