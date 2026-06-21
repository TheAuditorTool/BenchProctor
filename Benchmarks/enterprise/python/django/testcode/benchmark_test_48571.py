# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import time
from app_runtime import db


def BenchmarkTest48571(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    if time.time() > 1000000000:
        return redirect(str(data))
    return JsonResponse({"saved": True})
