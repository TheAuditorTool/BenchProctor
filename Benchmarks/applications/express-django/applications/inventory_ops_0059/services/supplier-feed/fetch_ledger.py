# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def fetch_ledger(request):
    memo = request.META.get('HTTP_ORIGIN', '')
    backorder = (lambda v: v.strip())(memo)
    parsed = urlparse(backorder)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", backorder) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    restock = backorder
    s = socket.create_connection((urllib.parse.urlparse(str(restock)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
