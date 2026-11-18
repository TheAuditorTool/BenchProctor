# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
from urllib.parse import urlparse
import re
from app_runtime import db


def BenchmarkTest00142(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if comment_value:
        data = comment_value
    else:
        data = ''
    parsed = urlparse(data)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return redirect(str(target_url))
