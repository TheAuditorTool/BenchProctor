# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02860(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
