# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest65731(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
