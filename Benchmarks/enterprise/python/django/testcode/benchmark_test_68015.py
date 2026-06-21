# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str
_shared_counter_lock = threading.Lock()

def BenchmarkTest68015(request):
    xml_value = request.body.decode('utf-8')
    data = FormData(payload=xml_value).payload
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
