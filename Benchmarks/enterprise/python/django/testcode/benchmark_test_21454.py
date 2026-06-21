# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21454(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return JsonResponse({"saved": True})
