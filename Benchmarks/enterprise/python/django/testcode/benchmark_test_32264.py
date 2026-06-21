# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32264(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
