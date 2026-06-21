# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32573(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    prefix = ''
    data = prefix + str(ua_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
