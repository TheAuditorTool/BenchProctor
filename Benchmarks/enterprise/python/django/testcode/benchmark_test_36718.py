# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request


def BenchmarkTest36718(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
