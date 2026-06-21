# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05900(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    int(str(data))
    return JsonResponse({"saved": True})
