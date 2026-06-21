# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20325(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
