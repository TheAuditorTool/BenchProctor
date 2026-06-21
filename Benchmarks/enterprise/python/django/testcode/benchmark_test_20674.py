# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from dataclasses import dataclass
from django.http import HttpResponse
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest20674(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = FormData(payload=header_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
