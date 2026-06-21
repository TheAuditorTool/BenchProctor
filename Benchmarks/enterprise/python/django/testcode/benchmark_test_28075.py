# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest28075(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
