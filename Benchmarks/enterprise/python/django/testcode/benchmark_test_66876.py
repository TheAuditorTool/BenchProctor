# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


def BenchmarkTest66876(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    defusedxml.ElementTree.fromstring(str(db_value))
    return JsonResponse({"saved": True})
