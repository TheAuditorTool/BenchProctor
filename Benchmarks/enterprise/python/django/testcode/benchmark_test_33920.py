# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33920(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    int(str(data))
    return JsonResponse({"saved": True})
