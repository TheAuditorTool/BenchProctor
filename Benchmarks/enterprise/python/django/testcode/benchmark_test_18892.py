# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest18892(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
