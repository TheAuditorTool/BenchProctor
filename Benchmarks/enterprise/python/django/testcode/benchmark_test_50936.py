# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import os


def BenchmarkTest50936(request):
    env_value = os.environ.get('USER_INPUT', '')
    parsed = urlparse(env_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = env_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
