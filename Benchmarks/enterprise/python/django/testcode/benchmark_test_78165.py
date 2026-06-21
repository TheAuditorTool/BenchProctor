# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78165(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
