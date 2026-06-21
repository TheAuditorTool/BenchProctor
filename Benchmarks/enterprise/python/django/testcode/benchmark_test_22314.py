# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest22314(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
