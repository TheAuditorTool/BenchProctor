# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def normalise_input(value):
    return value.strip()

def BenchmarkTest02406(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.post('http://api.prod.internal/data', data=str(target_url))
    return JsonResponse({"saved": True})
