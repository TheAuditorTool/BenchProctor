# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def to_text(value):
    return str(value).strip()

def BenchmarkTest66926(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = to_text(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
