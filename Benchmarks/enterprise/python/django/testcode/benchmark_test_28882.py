# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

def BenchmarkTest28882(request):
    user_id = request.GET.get('id', '')
    data = FormData(payload=user_id).payload
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
