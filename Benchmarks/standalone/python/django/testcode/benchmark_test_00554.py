# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from app_runtime import db


def BenchmarkTest00554(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(comment_value).strip()
        case _:
            data = str(comment_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
