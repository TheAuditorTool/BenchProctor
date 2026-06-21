# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest78114(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
