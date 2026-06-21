# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40233(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
