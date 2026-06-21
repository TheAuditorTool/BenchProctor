# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57793(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
