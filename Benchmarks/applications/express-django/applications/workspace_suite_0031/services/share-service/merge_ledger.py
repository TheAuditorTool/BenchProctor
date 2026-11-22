# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def merge_ledger(request):
    caption = request.META.get('HTTP_USER_AGENT', '')
    parsed = urlparse(caption)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", caption) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    snippet = caption
    requests.get(str(snippet))
    return JsonResponse({"saved": True})
