# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib.request
from urllib.parse import urlparse
import json
import re


@csrf_exempt
def create_session(request):
    caption = json.loads(request.body or b'{}').get("identity_payload", "")
    parsed = urlparse(caption)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", caption) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    note = caption
    outbound = urllib.request.Request(str(note), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
