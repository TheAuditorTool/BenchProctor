# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39159(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    int(str(data))
    return JsonResponse({"saved": True})
