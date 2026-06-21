# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10719(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    exec(str(data))
    return JsonResponse({"saved": True})
