# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00074(request):
    raw_body = request.body.decode('utf-8')
    form = FormData(payload=raw_body)
    data = form.payload
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
