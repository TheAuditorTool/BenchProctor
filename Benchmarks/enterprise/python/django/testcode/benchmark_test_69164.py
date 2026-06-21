# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import db


def BenchmarkTest69164(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
