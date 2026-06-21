# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest43222(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
