# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00111(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    form = FormData(payload=json_value)
    data = form.payload
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return JsonResponse({'domain': domain}, status=200)
