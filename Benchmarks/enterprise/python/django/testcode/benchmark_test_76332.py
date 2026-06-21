# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request


def BenchmarkTest76332(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', forwarded_ip):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = forwarded_ip
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
