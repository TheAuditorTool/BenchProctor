# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41648(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
