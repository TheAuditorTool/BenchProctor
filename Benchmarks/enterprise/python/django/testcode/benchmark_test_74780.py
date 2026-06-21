# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74780(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
