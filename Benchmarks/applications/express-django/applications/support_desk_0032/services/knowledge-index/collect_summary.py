# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def collect_summary(request):
    note = request.COOKIES.get('session_token', '')
    kind = 'json' if str(note).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            inquiry = str(note).strip()
        case _:
            inquiry = str(note)
    parsed = urlparse(inquiry)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    grievance = inquiry
    s = socket.create_connection((str(grievance), 80))
    s.close()
    return JsonResponse({"saved": True})
