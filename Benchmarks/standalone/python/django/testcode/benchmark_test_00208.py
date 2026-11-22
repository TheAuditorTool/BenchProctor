# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from urllib.parse import urlparse
import re


def BenchmarkTest00208(request):
    field_value = request.POST.get('field', '')
    data = f'{field_value!s}'
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    outbound = urllib.request.Request(str(target_url), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
