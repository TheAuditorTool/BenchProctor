# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest38751(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
