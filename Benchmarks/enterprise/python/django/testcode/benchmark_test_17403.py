# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17403(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
