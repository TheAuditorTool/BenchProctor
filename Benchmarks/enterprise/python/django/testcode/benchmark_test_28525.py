# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28525(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
