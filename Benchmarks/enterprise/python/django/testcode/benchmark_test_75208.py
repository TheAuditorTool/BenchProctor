# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75208(request):
    host_value = request.META.get('HTTP_HOST', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
