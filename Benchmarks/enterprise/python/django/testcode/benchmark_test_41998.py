# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def relay_value(value):
    return value

def BenchmarkTest41998(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = relay_value(referer_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
