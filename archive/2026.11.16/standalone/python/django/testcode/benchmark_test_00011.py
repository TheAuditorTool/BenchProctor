# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import db


def BenchmarkTest00011(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    digest = hashlib.sha256(str(comment_value).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
