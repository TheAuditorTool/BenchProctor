# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57043(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    prefix = ''
    data = prefix + str(origin_value)
    eval(str(data))
    return JsonResponse({"saved": True})
