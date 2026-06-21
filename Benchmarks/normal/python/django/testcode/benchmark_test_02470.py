# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import urllib.request
from app_runtime import db


def BenchmarkTest02470(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
