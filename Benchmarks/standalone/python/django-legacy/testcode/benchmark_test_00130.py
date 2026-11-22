# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
from django.http import HttpResponse
import re


def BenchmarkTest00130(request):
    raw_body = request.body.decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    resp = HttpResponse(status=302)
    resp['Location'] = str(target_url)
    return resp
