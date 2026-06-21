# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03363(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % str(referer_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
