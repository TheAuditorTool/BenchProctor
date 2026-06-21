# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33867(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    result = 100 / int(str(origin_value))
    return JsonResponse({"saved": True})
