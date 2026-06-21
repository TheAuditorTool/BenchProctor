# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest05275(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
