# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest03471(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
