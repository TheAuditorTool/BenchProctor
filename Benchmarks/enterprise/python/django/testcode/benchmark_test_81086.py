# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81086(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
