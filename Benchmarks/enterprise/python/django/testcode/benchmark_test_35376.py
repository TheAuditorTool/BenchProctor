# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from lxml import etree
from app_runtime import db


def normalise_input(value):
    return value.strip()

def BenchmarkTest35376(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return JsonResponse({"saved": True})
