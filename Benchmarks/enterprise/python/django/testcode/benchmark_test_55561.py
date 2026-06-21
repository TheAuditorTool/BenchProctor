# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest55561(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    int(str(data))
    return JsonResponse({"saved": True})
