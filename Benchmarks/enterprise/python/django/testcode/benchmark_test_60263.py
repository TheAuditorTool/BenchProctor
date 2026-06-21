# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60263(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
