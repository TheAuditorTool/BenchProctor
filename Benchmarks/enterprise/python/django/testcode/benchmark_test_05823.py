# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest05823(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = FormData(payload=auth_header).payload
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JsonResponse({'token': str(token)}, status=200)
