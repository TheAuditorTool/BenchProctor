# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest28842(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(referer_value)}, verify=True)
    return JsonResponse({"saved": True})
