# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53603(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = (lambda v: v.strip())(ua_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
