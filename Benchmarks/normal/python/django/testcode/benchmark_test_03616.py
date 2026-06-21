# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import socket


@dataclass
class FormData:
    payload: str

def BenchmarkTest03616(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
