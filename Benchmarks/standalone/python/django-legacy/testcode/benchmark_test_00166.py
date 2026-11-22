# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from urllib.parse import urlparse
import re
from app_runtime import db


def BenchmarkTest00166(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    outbound = urllib.request.Request(str(target_url), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
