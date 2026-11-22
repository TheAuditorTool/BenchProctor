# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest00001(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(comment_value).encode()), events=('end',)):
        element.clear()
    return JsonResponse({"saved": True})
