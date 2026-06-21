# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse


def BenchmarkTest78418(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    _resp = requests.get(str(target_url))
    exec(_resp.text)
    return JsonResponse({"saved": True})
