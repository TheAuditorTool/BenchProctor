# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest04656(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    defusedxml.ElementTree.fromstring(str(comment_value))
    return JsonResponse({"saved": True})
