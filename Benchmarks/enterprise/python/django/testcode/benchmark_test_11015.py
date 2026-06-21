# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import db


def BenchmarkTest11015(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    size = min(int(comment_value) if str(comment_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
