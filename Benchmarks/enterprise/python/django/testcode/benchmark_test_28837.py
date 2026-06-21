# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from dataclasses import dataclass
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest28837(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
