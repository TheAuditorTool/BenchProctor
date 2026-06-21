# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59078(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
