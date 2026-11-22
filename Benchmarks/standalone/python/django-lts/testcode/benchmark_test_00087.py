# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import io
from lxml import etree
from app_runtime import db


def BenchmarkTest00087(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    for _event, element in etree.iterparse(io.BytesIO(str(data).encode()), events=('end',), load_dtd=True, resolve_entities=True, no_network=False):
        element.clear()
    return JsonResponse({"saved": True})
