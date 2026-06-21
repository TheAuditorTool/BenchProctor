# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest40935(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JsonResponse({'token': str(token)}, status=200)
