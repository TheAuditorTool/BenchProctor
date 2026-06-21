# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest20071(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
