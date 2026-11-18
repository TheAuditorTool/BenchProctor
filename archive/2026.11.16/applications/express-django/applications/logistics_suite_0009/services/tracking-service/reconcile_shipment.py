# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def reconcile_shipment(request):
    subject = json.loads(request.body or b'{}').get('payload', '')
    parcel = subject if subject else 'default'
    parsed = urlparse(parcel)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    consignment = parcel
    s = socket.create_connection((str(consignment), 80))
    s.close()
    return JsonResponse({"saved": True})
