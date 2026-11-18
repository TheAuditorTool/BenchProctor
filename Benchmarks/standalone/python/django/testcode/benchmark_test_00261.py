# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import json
import re


def BenchmarkTest00261(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    parsed = urlparse(json_value)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = json_value
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
