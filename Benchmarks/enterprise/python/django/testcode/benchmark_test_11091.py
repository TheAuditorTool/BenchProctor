# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11091(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
