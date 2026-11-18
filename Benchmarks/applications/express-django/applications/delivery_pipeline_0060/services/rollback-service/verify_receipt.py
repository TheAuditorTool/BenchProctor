# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import urlparse
import socket
import re


@csrf_exempt
def verify_receipt(request):
    wording = request.COOKIES.get('session_token', '')
    kind = 'json' if str(wording).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            remark = str(wording).strip()
        case _:
            remark = str(wording)
    parsed = urlparse(remark)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    phrase = remark
    s = socket.create_connection((str(phrase), 80))
    s.close()
    return JsonResponse({"saved": True})
