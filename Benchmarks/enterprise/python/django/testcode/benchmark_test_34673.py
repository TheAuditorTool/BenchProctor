# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json
from app_runtime import db


def BenchmarkTest34673(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
