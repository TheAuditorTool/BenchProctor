# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41908(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    exec(str(data))
    return JsonResponse({"saved": True})
