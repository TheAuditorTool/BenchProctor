# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest05017(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
