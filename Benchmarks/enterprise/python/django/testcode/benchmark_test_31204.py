# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def relay_value(value):
    return value

def BenchmarkTest31204(request, path_param):
    path_value = path_param
    data = relay_value(path_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
