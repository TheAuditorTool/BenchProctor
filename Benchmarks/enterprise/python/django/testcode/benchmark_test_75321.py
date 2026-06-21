# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75321(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
