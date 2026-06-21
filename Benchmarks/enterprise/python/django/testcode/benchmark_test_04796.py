# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest04796(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
