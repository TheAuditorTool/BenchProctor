# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02605(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
