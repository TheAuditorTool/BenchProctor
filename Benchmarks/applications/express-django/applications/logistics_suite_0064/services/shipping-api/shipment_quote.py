# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import json
import re


@csrf_exempt
def quote_shipment(request):
    footnote = json.loads(request.body or b'{}').get("shipping_payload", "")
    parsed = urlparse(footnote)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    consignment = footnote
    requests.get(str(consignment))
    return JsonResponse({"saved": True})
