# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest37964(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = to_text(referer_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})
