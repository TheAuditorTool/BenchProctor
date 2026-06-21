# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest74351(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    int(str(data))
    return JsonResponse({"saved": True})
