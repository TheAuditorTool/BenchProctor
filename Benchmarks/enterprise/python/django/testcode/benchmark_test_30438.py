# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest30438(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    parsed = urlparse(data)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
