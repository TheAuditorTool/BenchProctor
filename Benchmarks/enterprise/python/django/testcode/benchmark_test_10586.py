# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest10586(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = FormData(payload=origin_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
