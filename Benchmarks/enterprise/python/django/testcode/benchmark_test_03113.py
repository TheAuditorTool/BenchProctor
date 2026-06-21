# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03113(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
