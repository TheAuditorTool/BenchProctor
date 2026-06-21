# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest23524(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
