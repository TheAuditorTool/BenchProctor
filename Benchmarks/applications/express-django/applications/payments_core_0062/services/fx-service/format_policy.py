# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def format_policy(request, path_param):
    headline = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    disbursement = normalize(headline)
    parsed = urlparse(disbursement)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    remittance = disbursement
    s = socket.create_connection((str(remittance), 80))
    s.close()
    return JsonResponse({"saved": True})
