# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12689(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
