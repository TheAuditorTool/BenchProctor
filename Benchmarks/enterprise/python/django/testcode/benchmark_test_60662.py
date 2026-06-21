# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60662(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
