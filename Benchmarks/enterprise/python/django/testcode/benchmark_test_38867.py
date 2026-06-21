# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38867(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
