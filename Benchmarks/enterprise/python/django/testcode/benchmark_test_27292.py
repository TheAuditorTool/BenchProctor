# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27292(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
