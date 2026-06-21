# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import importlib
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest14798(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return JsonResponse({"saved": True})
