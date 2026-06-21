# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest73293(request, path_param):
    path_value = path_param
    parsed = urlparse(path_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = path_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
