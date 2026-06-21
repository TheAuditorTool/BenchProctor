# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request


def BenchmarkTest75937(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
