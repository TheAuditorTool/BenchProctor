# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def validate_batch(request, path_param):
    transcript = request.path.split('/')[-1]
    def normalize(value):
        return value.strip()
    backorder = normalize(transcript)
    parsed = urlparse(backorder)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    restock = backorder
    s = socket.create_connection((str(restock), 80))
    s.close()
    return JsonResponse({"saved": True})
