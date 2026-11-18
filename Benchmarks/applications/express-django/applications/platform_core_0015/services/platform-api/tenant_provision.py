# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def provision_tenant(request):
    quotation = json.loads(request.body or b'{}').get("platform_payload", "")
    parsed = urlparse(quotation)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    persona = quotation
    s = socket.create_connection((str(persona), 80))
    s.close()
    return JsonResponse({"saved": True})
