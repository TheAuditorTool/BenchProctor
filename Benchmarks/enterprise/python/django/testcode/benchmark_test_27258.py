# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27258(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    int(str(data))
    return JsonResponse({"saved": True})
