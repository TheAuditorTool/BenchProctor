# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest29192(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
