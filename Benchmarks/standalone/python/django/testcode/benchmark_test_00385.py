# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest00385(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = []
    for token in str(comment_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
