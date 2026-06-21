# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request


def BenchmarkTest67758(request):
    multipart_value = request.POST.get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = multipart_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
