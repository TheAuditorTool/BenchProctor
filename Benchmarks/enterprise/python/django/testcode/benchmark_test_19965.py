# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import requests


def BenchmarkTest19965(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = unquote(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
