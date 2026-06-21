# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import json


def BenchmarkTest70088(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    parsed = urlparse(graphql_var)
    if parsed.hostname not in ('api.prod.internal', 'cdn.pycdn.io'):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = graphql_var
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
