# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39707(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
