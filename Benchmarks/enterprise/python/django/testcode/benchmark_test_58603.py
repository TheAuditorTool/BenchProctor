# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest58603(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
