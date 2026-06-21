# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54135(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
