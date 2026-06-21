# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33501(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
