# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def ensure_str(value):
    return str(value)

def BenchmarkTest22449(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ensure_str(referer_value)
    int(str(data))
    return JsonResponse({"saved": True})
