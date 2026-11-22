# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import urllib.parse
import re


@csrf_exempt
def quote_shipment(request):
    remark = json.loads(request.body or b'{}').get("shipping_payload", "")
    parsed = urlparse(remark)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remark) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    consignment = remark
    s = socket.create_connection((urllib.parse.urlparse(str(consignment)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
