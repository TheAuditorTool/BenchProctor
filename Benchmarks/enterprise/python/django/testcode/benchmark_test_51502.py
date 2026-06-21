# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import ast


_shared_counter_lock = threading.Lock()

def BenchmarkTest51502(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
