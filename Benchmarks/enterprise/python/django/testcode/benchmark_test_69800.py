# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import re


@dataclass
class FormData:
    payload: str

def BenchmarkTest69800(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
