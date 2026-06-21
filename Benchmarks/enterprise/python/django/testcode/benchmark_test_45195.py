# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45195(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})
