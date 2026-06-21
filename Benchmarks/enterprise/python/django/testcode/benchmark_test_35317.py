# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest35317(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    json.loads(data)
    return JsonResponse({"saved": True})
