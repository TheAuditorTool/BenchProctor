# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest53190(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
