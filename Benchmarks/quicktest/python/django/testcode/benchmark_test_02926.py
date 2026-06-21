# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02926(request):
    host_value = request.META.get('HTTP_HOST', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
