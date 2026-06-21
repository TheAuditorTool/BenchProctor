# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest78651(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
