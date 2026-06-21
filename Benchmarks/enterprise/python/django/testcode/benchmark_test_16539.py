# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16539(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    eval(str(data))
    return JsonResponse({"saved": True})
