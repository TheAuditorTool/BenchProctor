# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest63135(request):
    multipart_value = request.POST.get('multipart_field', '')
    parsed = urlparse(multipart_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = multipart_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
