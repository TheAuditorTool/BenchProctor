# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib.request
from urllib.parse import urlparse
import re
from app_runtime import db


@csrf_exempt
def build_checkpoint(request):
    citation = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    parcel = normalize(citation)
    parsed = urlparse(parcel)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", parcel) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    consignment = parcel
    outbound = urllib.request.Request(str(consignment), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return JsonResponse({"saved": True})
