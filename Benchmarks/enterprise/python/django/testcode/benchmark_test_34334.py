# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest34334(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return JsonResponse({"saved": True})
