# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01590(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
