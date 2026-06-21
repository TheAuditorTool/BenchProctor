# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest70652(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
