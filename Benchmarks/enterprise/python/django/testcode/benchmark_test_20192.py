# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20192(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
