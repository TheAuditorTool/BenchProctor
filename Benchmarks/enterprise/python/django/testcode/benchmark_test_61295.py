# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest61295(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
