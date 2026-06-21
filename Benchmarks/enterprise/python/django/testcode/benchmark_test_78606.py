# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78606(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
