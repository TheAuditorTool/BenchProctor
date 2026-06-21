# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest15531(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
