# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request


def BenchmarkTest66051(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
