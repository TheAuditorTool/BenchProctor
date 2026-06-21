# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44288(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = str(referer_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
