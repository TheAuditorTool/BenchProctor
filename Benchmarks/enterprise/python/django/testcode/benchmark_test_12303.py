# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12303(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return JsonResponse({"saved": True})
