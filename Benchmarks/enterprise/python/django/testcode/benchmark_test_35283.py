# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
from urllib.parse import unquote


_shared_counter_lock = threading.Lock()

def BenchmarkTest35283(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
