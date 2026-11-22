# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
import re
from app_runtime import db


def BenchmarkTest00013(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    parsed = urlparse(data)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", data) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return HttpResponseRedirect(str(target_url))
