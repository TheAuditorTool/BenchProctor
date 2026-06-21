# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest73558(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
