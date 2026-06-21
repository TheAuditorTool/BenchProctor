# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest21838(request, path_param):
    path_value = path_param
    data = FormData(payload=path_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
