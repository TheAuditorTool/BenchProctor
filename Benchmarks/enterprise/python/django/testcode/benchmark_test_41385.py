# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest41385(request):
    raw_body = request.body.decode('utf-8')
    data = FormData(payload=raw_body).payload
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
