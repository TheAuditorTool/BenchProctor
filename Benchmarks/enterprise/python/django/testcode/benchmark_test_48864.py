# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest48864(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({"saved": True})
