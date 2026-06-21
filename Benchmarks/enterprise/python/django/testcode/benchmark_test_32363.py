# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32363(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    eval(str(data))
    return JsonResponse({"saved": True})
