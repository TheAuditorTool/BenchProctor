# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest21326(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
