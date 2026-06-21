# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest29137(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
