# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest27851(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ' '.join(str(db_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
