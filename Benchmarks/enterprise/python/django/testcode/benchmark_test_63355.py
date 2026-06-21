# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63355(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = str(ua_value).replace('\x00', '')
    int(str(data))
    return JsonResponse({"saved": True})
