# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
import json


def BenchmarkTest58625(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
