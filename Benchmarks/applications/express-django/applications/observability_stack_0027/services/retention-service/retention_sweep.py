# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import json
import re


@csrf_exempt
def sweep_retention(request):
    headline = json.loads(request.body or b'{}').get("telemetry_payload", "")
    parsed = urlparse(headline)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", headline) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    cohort = headline
    requests.get(str(cohort))
    return JsonResponse({"saved": True})
