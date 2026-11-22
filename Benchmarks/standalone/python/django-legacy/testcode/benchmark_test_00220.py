# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import json
import re


def BenchmarkTest00220(request):
    graphql_var = json.loads(request.body or b'{}').get('variables', {}).get('input', '')
    data = f'{graphql_var!s}'
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
