# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import db


def BenchmarkTest55163(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
