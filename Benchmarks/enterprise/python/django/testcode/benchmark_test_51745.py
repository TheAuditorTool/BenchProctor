# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51745(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    eval(str(data))
    return JsonResponse({"saved": True})
