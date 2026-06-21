# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import urllib.request
from app_runtime import db


def BenchmarkTest14633(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', comment_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(processed)).read()
    return JsonResponse({"saved": True})
