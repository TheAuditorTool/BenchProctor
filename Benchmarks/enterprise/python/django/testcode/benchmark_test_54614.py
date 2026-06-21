# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest54614(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
