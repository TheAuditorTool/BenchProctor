# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os
from app_runtime import db


def BenchmarkTest62413(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    entries = os.listdir(str(data))
    return JsonResponse({'listing': entries}, status=200)
