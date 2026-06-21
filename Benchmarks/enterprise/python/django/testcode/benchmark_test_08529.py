# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08529(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
