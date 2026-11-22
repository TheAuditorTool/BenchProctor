# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib.request
from urllib.parse import urlparse
import re


@csrf_exempt
def audit_checkpoint(request):
    memo = request.META.get('HTTP_AUTHORIZATION', '')
    ledger = bytes.fromhex(memo).decode('utf-8', 'ignore')
    parsed = urlparse(ledger)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", ledger) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    remittance = ledger
    outbound = urllib.request.Request(str(remittance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
