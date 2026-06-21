# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest46795(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    eval(str(data))
    return JsonResponse({"saved": True})
