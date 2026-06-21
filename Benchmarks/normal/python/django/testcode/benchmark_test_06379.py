# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def coalesce_blank(value):
    return value or ''

def BenchmarkTest06379(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return JsonResponse({"saved": True})
