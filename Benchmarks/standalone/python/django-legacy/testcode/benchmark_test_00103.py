# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import os
from django.http import HttpResponse
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00103(request):
    env_value = os.environ.get('APP_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    resp = HttpResponse(status=302)
    resp['Location'] = str(target_url)
    return resp
