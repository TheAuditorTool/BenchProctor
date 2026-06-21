# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32697(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
