# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest75269(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
