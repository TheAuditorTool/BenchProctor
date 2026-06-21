# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest34813(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = FormData(payload=forwarded_ip).payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
