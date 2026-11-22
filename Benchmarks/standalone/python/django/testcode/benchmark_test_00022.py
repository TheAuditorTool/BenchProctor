# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
import re


def BenchmarkTest00022(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ' '.join(parts)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponseRedirect(str(target_url))
