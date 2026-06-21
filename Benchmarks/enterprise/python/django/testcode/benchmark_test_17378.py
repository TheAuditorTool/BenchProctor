# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17378(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    exec(str(data))
    return JsonResponse({"saved": True})
