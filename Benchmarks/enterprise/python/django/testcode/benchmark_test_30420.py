# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30420(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    eval(str(data))
    return JsonResponse({"saved": True})
