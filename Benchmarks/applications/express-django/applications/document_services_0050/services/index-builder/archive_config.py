# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def archive_config(request):
    citation = request.GET.get('id', '')
    dossier = unquote(citation)
    parsed = urlparse(dossier)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", dossier) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    addendum = dossier
    requests.get(str(addendum))
    return JsonResponse({"saved": True})
