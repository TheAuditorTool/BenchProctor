# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from urllib.parse import unquote
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def enrich_header(request):
    headline = request.GET.get('id', '')
    disbursement = unquote(headline)
    parsed = urlparse(disbursement)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", disbursement) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    remittance = disbursement
    requests.get(str(remittance))
    return JsonResponse({"saved": True})
