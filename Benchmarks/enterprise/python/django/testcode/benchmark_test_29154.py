# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import json


def BenchmarkTest29154(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    parsed = urlparse(json_value)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = json_value
    return redirect(str(target_url))
