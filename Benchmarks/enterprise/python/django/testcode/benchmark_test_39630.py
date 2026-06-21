# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39630(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
