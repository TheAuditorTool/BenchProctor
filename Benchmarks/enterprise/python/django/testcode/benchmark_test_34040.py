# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34040(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
