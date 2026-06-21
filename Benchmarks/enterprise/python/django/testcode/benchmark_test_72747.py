# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72747(request):
    host_value = request.META.get('HTTP_HOST', '')
    size = min(int(host_value) if str(host_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
