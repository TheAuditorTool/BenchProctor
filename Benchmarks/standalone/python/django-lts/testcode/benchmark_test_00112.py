# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import re


def BenchmarkTest00112(request):
    raw_body = request.body.decode('utf-8')
    parsed = urlparse(raw_body)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", raw_body) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = raw_body
    requests.get(str(target_url))
    return JsonResponse({"saved": True})
