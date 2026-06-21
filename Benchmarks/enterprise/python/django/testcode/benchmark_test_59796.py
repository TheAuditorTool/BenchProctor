# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59796(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
