# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest54688(request):
    upload_name = request.FILES['upload'].name
    data = FormData(payload=upload_name).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
