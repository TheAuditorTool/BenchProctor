# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36191(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    prefix = ''
    data = prefix + str(referer_value)
    eval(str(data))
    return JsonResponse({"saved": True})
