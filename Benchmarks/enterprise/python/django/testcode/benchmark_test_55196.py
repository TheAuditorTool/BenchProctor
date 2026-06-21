# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest55196(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
