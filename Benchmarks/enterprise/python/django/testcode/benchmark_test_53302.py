# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest53302(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
