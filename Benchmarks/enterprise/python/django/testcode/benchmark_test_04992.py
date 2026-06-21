# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04992(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
