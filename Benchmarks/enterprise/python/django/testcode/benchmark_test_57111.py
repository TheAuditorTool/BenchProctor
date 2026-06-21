# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57111(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
