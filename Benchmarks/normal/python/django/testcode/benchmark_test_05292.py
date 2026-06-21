# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05292(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
