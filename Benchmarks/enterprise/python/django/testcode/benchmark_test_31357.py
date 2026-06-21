# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest31357(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return JsonResponse({"saved": True})
