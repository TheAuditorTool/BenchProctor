# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import json
import socket
import re


@csrf_exempt
def reconcile_profile(request):
    excerpt = json.loads(request.body or b'{}').get('payload', '')
    dossier = excerpt if excerpt else 'default'
    parsed = urlparse(dossier)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    addendum = dossier
    s = socket.create_connection((str(addendum), 80))
    s.close()
    return JsonResponse({"saved": True})
