# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from lxml import etree
from app_runtime import db


def BenchmarkTest57419(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(db_value).encode(), _parser)
    return JsonResponse({"saved": True})
