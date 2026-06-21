# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest02075(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
