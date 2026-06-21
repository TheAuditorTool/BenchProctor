# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest65737(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
