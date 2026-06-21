# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest34726(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    requests.post('http://api.prod.internal/data', data=str(referer_value))
    return JsonResponse({"saved": True})
