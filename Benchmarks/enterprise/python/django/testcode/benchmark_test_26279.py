# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re


request_state: dict[str, str] = {}

def BenchmarkTest26279(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
