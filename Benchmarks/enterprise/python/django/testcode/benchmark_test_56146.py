# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest56146(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
