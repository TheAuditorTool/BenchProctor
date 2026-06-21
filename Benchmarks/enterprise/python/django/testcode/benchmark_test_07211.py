# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db, auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest07211(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
