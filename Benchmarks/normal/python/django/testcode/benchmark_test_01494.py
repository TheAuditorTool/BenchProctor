# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


_shared_counter_lock = threading.Lock()

def BenchmarkTest01494(request):
    upload_name = request.FILES['upload'].name
    prefix = ''
    data = prefix + str(upload_name)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
