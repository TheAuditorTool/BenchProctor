# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45812(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
