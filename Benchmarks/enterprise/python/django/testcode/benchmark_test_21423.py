# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21423(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
