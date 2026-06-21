# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest09950(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value:.200s}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
