# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from urllib.parse import urlparse
import re


@csrf_exempt
def publish_schedule(request):
    heading = request.META.get('HTTP_USER_AGENT', '')
    parsed = urlparse(heading)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", heading) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    byline = heading
    requests.get(str(byline))
    return JsonResponse({"saved": True})
