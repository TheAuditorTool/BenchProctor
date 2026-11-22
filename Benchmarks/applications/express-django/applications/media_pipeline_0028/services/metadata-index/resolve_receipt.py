# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def resolve_receipt(request):
    citation = request.GET.get('id', '')
    rendition = unquote(citation)
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    montage = rendition
    requests.get(str(montage))
    return JsonResponse({"saved": True})
