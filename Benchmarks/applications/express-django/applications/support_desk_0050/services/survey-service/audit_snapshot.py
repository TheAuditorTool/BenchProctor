# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def audit_snapshot(request, path_param):
    remark = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    inquiry = normalize(remark)
    parsed = urlparse(inquiry)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    grievance = inquiry
    s = socket.create_connection((str(grievance), 80))
    s.close()
    return JsonResponse({"saved": True})
