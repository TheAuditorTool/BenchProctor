# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest68616(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
