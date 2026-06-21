# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02138(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
