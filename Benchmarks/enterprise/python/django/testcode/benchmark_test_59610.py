# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59610(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
