# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest61743(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    pending = list(str(referer_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    pickle.loads(data.encode('latin-1'))
    return JsonResponse({"saved": True})
