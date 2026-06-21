# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest47220(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return JsonResponse({"saved": True})
