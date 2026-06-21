# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest64303(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
