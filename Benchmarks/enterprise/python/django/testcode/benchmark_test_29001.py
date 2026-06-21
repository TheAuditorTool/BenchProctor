# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29001(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    eval(str(data))
    return JsonResponse({"saved": True})
