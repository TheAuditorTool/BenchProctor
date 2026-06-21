# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request


def BenchmarkTest60083(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = auth_header
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
