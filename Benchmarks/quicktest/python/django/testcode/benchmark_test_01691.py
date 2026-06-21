# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest01691(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = FormData(payload=ua_value).payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
