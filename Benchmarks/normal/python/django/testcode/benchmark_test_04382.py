# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import time
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest04382(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    if time.time() > 1000000000:
        return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
    return JsonResponse({"saved": True})
