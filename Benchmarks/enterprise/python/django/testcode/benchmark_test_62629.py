# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62629(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    eval(str(data))
    return JsonResponse({"saved": True})
