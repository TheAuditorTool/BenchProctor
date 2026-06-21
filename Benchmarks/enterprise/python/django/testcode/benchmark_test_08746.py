# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08746(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    eval(str(data))
    return JsonResponse({"saved": True})
