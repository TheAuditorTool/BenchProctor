# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest03020(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
