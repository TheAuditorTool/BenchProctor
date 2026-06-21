# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest11004(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
