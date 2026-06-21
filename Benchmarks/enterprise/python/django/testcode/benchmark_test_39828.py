# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39828(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
