# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import urllib.parse
import re


@csrf_exempt
def merge_roster(request):
    citation = request.META.get('HTTP_ORIGIN', '')
    consignment = (lambda v: v.strip())(citation)
    parsed = urlparse(consignment)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", consignment) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    parcel = consignment
    s = socket.create_connection((urllib.parse.urlparse(str(parcel)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
