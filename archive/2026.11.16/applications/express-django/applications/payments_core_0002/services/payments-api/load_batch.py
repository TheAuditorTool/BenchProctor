# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def load_batch(request):
    subtitle = json.loads(request.body or b'{}').get('payload', '')
    ledger = subtitle if subtitle else 'default'
    parsed = urlparse(ledger)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    remittance = ledger
    s = socket.create_connection((str(remittance), 80))
    s.close()
    return JsonResponse({"saved": True})
