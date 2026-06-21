# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74058(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
