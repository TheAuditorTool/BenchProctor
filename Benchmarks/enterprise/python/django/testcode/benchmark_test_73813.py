# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest73813(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    auth_check('user', data)
    return JsonResponse({"saved": True})
