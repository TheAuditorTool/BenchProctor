# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33154(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    size = min(int(origin_value) if str(origin_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
