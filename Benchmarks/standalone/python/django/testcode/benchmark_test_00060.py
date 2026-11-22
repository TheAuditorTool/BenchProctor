# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest00060(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = f'{comment_value!s}'
    for _event, element in defusedxml.ElementTree.iterparse(io.BytesIO(str(data).encode()), events=('end',)):
        element.clear()
    return JsonResponse({"saved": True})
