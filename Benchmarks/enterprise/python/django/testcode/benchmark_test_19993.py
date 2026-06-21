# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19993(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
