# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41846(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})
