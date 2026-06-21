# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest33350(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
