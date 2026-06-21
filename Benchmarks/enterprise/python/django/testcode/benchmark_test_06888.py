# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest06888(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return JsonResponse({"saved": True})
