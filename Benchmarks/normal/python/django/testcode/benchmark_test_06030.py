# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import os
from django.http import HttpResponse


@dataclass
class FormData:
    payload: str

def BenchmarkTest06030(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
