# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import json
import urllib.request


def BenchmarkTest71381(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', json_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = json_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
