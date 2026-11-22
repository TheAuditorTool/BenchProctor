# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
import re


def BenchmarkTest00001(request):
    field_value = request.POST.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponseRedirect(str(target_url))
