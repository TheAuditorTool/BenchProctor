# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest29554(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
