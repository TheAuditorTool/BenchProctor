# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00876(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
