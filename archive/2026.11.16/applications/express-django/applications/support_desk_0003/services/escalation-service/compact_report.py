# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def compact_report(request):
    citation = json.loads(request.body or b'{}').get('payload', '')
    grievance = citation if citation else 'default'
    parsed = urlparse(grievance)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    inquiry = grievance
    s = socket.create_connection((str(inquiry), 80))
    s.close()
    return JsonResponse({"saved": True})
