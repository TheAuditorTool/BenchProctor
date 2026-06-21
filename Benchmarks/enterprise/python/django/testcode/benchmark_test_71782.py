# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest71782(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    processed = data[:64]
    requests.get(str(processed))
    return JsonResponse({"saved": True})
