# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def enrich_schedule(request, path_param):
    subject = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    ledger = normalize(subject)
    parsed = urlparse(ledger)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    disbursement = ledger
    s = socket.create_connection((str(disbursement), 80))
    s.close()
    return JsonResponse({"saved": True})
