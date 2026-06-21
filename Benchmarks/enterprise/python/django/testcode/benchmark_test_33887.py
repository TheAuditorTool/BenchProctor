# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest33887(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.post('http://api.prod.internal/data', data=str(target_url))
    return JsonResponse({"saved": True})
