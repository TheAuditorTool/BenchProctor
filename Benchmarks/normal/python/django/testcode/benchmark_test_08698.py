# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import requests


def BenchmarkTest08698(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    data = api_value if api_value else 'default'
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
