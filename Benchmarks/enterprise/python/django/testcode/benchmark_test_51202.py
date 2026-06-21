# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest51202(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
