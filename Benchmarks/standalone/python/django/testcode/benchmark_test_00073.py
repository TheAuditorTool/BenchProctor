# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def BenchmarkTest00073(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(comment_value).encode(), _parser)
    return JsonResponse({"saved": True})
