# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
import json
import re


def BenchmarkTest00013(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    pending = list(str(json_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponseRedirect(str(target_url))
