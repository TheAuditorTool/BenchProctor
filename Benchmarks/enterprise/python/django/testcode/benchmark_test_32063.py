# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest32063(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
