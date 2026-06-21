# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47971(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    eval(str(data))
    return JsonResponse({"saved": True})
