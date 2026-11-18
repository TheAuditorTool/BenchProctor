# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def export_summary(request):
    phrase = request.COOKIES.get('session_token', '')
    kind = 'json' if str(phrase).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parcel = str(phrase).strip()
        case _:
            parcel = str(phrase)
    parsed = urlparse(parcel)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    consignment = parcel
    s = socket.create_connection((str(consignment), 80))
    s.close()
    return JsonResponse({"saved": True})
