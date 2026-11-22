# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
from django.http import HttpResponse
import re


def BenchmarkTest00049(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    resp = HttpResponse(status=302)
    resp['Location'] = str(target_url)
    return resp
