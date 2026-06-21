# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest18926(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
