# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest40431(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
