# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def merge_receipt(request):
    paragraph = request.GET.get('id', '')
    persona = unquote(paragraph)
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    blurb = persona
    requests.get(str(blurb))
    return JsonResponse({"saved": True})
