# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81291(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
