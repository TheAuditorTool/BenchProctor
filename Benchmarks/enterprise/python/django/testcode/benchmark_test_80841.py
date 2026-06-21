# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80841(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = bytearray(int(ua_value) if str(ua_value).isdigit() else 0)
    return JsonResponse({"saved": True})
