# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest01261(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
