# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest78676(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
