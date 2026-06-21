# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db, auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest75694(request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    if not auth_check(str(data), request.session.get('token')):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
