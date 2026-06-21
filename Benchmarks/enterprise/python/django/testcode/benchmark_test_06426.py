# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest06426(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
