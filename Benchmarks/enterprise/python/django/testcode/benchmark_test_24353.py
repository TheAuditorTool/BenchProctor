# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24353(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
