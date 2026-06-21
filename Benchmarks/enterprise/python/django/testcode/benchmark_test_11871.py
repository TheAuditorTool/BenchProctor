# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request
from app_runtime import db


def BenchmarkTest11871(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
