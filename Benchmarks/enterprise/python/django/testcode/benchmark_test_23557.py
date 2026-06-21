# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

def BenchmarkTest23557(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return JsonResponse({"saved": True})
