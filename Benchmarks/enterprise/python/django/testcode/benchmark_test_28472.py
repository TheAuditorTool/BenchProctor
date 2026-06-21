# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28472(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
