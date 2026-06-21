# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest35140(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
