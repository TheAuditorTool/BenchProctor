# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest01662(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
