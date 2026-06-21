# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78940(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
