# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75927(request):
    host_value = request.META.get('HTTP_HOST', '')
    int(str(host_value))
    return JsonResponse({"saved": True})
