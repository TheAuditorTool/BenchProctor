# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80750(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
